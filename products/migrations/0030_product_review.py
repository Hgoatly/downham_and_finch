# Generated by Django 3.1.7 on 2021-06-16 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_review_item'),
        ('products', '0029_delete_fabricchoice'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='review',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='review.review'),
        ),
    ]
