# Generated by Django 4.0.6 on 2022-07-22 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.IntegerField(unique=True, verbose_name='Заказ №'),
        ),
    ]
