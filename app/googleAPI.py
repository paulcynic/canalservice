from oauth2client.service_account import ServiceAccountCredentials
import gspread


# If modifying these scopes, delete the file token.json.
SCOPES = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive.file',
        'https://www.googleapis.com/auth/drive',
        ]

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1jupyBDOGP8xpNYsdDhtyucU_zm3bh6NMyK_vZRTabYQ'
SAMPLE_RANGE_NAME = 'A2:D1000'
CREDENTIALS_FILE = 'creds.json'


def fetch_data():
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTIALS_FILE, SCOPES)
    client = gspread.authorize(credentials)
    sheet = client.open("canalservice_test").sheet1
    data =  sheet.get_all_records()
    row = sheet.row_values(3)
    col = sheet.col_values(3)
    cell = sheet.cell(1, 2).value
    print(row)
    print(cell)
    insertRow = ["hello", 5, "red", "blue"]
    #sheet.insert_row(insertRow, 4)
    #sheet.delete_rows(4)
    sheet.update_cell(2,2, "changed")
    orders = []
    #try:
        #service = build('sheets', 'v4', http=httpAuth)
        # Call the Sheets API
        #result = service.spreadsheets().values().get(
        #        spreadsheetId=SAMPLE_SPREADSHEET_ID,
        #        range=SAMPLE_RANGE_NAME,
        #        majorDimension='ROWS'
        #        ).execute()
        #values = result.get('values', ())

        #if not values:
        #    print('No data found.')
        #    return []
        #for value in values:
        #    order = {}
        #    order["number"] = value[0]
        #    order["order_id"] = value[1]
        #    order["price_usd"] = value[2]
        #    order["delivery_date"] = value[3]
        #    orders.append(order)

    return orders
fetch_data()
