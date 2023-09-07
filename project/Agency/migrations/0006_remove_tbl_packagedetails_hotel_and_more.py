# Generated by Django 4.2.1 on 2023-06-06 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agency', '0005_alter_tbl_packagedetails_hotel_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_packagedetails',
            name='hotel',
        ),
        migrations.RemoveField(
            model_name='tbl_packagedetails',
            name='meal',
        ),
        migrations.AddField(
            model_name='tbl_packagedetails',
            name='hotel',
            field=models.ManyToManyField(to='Agency.tbl_hoteldetails'),
        ),
        migrations.AddField(
            model_name='tbl_packagedetails',
            name='meal',
            field=models.ManyToManyField(to='Agency.tbl_mealdetails'),
        ),
    ]
