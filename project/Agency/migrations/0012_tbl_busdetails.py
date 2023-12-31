# Generated by Django 4.2.1 on 2023-06-07 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agency', '0011_tbl_dayhighlights'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_busdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_regno', models.CharField(max_length=40)),
                ('bus_type', models.CharField(max_length=20)),
                ('bus_seatcapacity', models.IntegerField()),
                ('bus_image', models.FileField(upload_to='busdocs/')),
                ('bus_status', models.IntegerField(default=0)),
            ],
        ),
    ]
