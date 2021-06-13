# Generated by Django 3.1.7 on 2021-06-05 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254)),
                ('content', models.TextField(max_length=800)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]