from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.status import HTTP_200_OK, HTTP_405_METHOD_NOT_ALLOWED
from rest_framework.decorators import api_view
from .serializers import OrderSerializer
from .services import delete_difference, fetch_data, get_price, get_xml
from canal.models import Order


# Create your views here.
@api_view(['GET'])
def orders(request):
    if request.method == 'GET':
        orders=fetch_data()
        delete_difference(orders)
        price = get_price(get_xml())
        print(price)
        for order in orders:
            order["price_rub"] = round((price * float(order["price_usd"])), 2)
            try:
                instance = Order.objects.get(order_id=order["order_id"])
            except Order.DoesNotExist:
                instance = None
            serializer = OrderSerializer(instance, data=order, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
        return Response(status=HTTP_200_OK)
    else:
        return Response(status=HTTP_405_METHOD_NOT_ALLOWED)
