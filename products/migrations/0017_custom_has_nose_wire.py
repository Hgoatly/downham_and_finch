# Generated by Django 3.1.7 on 2021-05-03 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20210503_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='custom',
            name='has_nose_wire',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]