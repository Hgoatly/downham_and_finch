# Generated by Django 3.1.7 on 2021-04-14 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20210414_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.DeleteModel(
            name='Size',
        ),
    ]
