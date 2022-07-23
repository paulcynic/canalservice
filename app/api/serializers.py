from rest_framework import serializers

from canal.models import Order

class OrderSerializer(serializers.ModelSerializer):
#    def create(self, validated_data):
#        return Order.objects.create(**validated_data)
#
#    def update(self, instance, validated_data):
#        instance.number = validated_data.get('number', instance.number)
#        instance.order_id = validated_data.get('order_id', instance.order_id)
#        instance.price_usd = validated_data.get('price_usd', instance.price_usd)
#        instance.price_rub = validated_data.get('price_rub', instance.price_rub)
#        instance.delivery_date = validated_data.get('delivery_date', instance.delivery_date)
#        instance.save()
#        return instance
#
    class Meta:
        model = Order
        fields = ('number', 'order_id', 'price_usd', 'price_rub', 'delivery_date')
