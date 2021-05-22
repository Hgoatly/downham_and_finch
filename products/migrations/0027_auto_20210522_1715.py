# Generated by Django 3.1.7 on 2021-05-22 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_product_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='fabricchoice',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product'),
        ),
        migrations.AddField(
            model_name='product',
            name='fabric_choice',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
