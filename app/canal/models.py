from django.db import models


class Order(models.Model):
    number = models.IntegerField(verbose_name='№')
    order_id = models.IntegerField(primary_key=True, verbose_name='Заказ №')
    price_usd = models.DecimalField(max_digits=16, decimal_places=2, null=True, blank=True, verbose_name='Стоимость,$')
    price_rub = models.DecimalField(max_digits=16, decimal_places=2, null=True, blank=True, verbose_name='Стоимость в руб.')
    delivery_date = models.DateField(null=True, blank=True, db_index=True, verbose_name='Срок поставки')

    class Meta:
        verbose_name_plural = 'Заказы'
        verbose_name = 'Заказ'
        ordering = ['number']
