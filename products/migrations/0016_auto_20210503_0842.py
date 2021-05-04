# Generated by Django 3.1.7 on 2021-05-03 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20210503_0822'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='custom',
            name='fabric',
        ),
        migrations.RemoveField(
            model_name='fabricchoice',
            name='fabric',
        ),
        migrations.AddField(
            model_name='custom',
            name='has_fabric_choice',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]