# Generated by Django 3.1.7 on 2021-05-08 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0024_fabricchoice_display_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fabricchoice',
            name='display_name',
            field=models.CharField(max_length=200),
        ),
    ]