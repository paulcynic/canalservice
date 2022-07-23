#  pip install --upgrade google-api-python-client oauth2client
from __future__ import print_function

import httplib2
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import requests
from lxml import etree

from canal.models import Order


# URL of CBR for currency price (price_rub)
URL = "http://www.cbr.ru/scripts/XML_daily.asp"

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1jupyBDOGP8xpNYsdDhtyucU_zm3bh6NMyK_vZRTabYQ'
SAMPLE_RANGE_NAME = 'A2:D1000'
CREDENTIALS_FILE = 'creds.json'


def fetch_data():
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTIALS_FILE, SCOPES)
    httpAuth = credentials.authorize(httplib2.Http())
    orders = []
    try:
        service = build('sheets', 'v4', http=httpAuth)
        # Call the Sheets API
        result = service.spreadsheets().values().get(
                spreadsheetId=SAMPLE_SPREADSHEET_ID,
                range=SAMPLE_RANGE_NAME,
                majorDimension='ROWS'
                ).execute()
        values = result.get('values', ())

        if not values:
            print('No data found.')
            return
        for value in values:
            order = {}
            order["number"] = value[0]
            order["order_id"] = value[1]
            order["price_usd"] = value[2]
            order["delivery_date"] = value[3]
            orders.append(order)

    except HttpError as err:
        print(err)
        order = {}
        order["number"] = None
        order["order_id"] = None
        order["price_usd"] = None
        order["delivery_date"] = None
        orders.append(order)
        return []
    return orders


def get_xml(url: str = URL):
    try:
        res = requests.get(url)
        res.raise_for_status()
    except requests.HTTPError as e:
        print(e)
        return None
    return res.content

def get_price(xml_content):
    try:
        root = etree.fromstring(xml_content)
        resp = root.xpath(f"//Valute[@ID='R01235']/Value")
        price = resp[0].text.replace(",", ".")
    except Exception as e:
        print(e)
        return float(0)
    return float(price)


def delete_difference(orders):
    google_sheet_list = [int(order["order_id"]) for order in orders]
    deleted_orders = Order.objects.exclude(order_id__in=google_sheet_list)
    deleted_orders.delete()
    return deleted_orders
