# Generated by Django 3.1.7 on 2021-05-03 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20210503_0815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='custom',
            name='product_type',
        ),
        migrations.AlterField(
            model_name='fabricchoice',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]