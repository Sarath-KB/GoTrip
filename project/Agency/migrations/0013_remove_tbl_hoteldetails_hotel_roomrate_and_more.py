# Generated by Django 4.2.1 on 2023-06-07 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Agency', '0012_tbl_busdetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_hoteldetails',
            name='hotel_roomrate',
        ),
        migrations.RemoveField(
            model_name='tbl_mealdetails',
            name='meal_rate',
        ),
    ]
