# Generated by Django 4.2.1 on 2023-07-12 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agency', '0018_remove_tbl_busdetails_bus_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_dayhighlights',
            name='day_image',
            field=models.FileField(null=True, upload_to='daydocs/'),
        ),
    ]
