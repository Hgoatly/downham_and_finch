# Generated by Django 3.1.7 on 2021-05-08 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_deliveryaddress_phone_number'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DeliveryAddress',
        ),
    ]