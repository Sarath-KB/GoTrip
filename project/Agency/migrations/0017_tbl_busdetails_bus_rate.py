# Generated by Django 4.2.1 on 2023-06-19 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agency', '0016_tbl_packagedetails_package_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_busdetails',
            name='bus_rate',
            field=models.CharField(default=0, max_length=30),
        ),
    ]
