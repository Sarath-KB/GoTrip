# Generated by Django 4.2.1 on 2023-06-19 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Agency', '0018_remove_tbl_busdetails_bus_rate'),
        ('Guest', '0007_tbl_agencyregister_agency_status'),
        ('User', '0005_tbl_payement'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_busbooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bbooking_date', models.DateField(auto_now=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('from_loc', models.DateField(max_length=50)),
                ('to_loc', models.CharField(max_length=50)),
                ('passengers', models.IntegerField()),
                ('bbooking_amount', models.CharField(max_length=30)),
                ('btotal_amount', models.CharField(max_length=30)),
                ('bbooking_status', models.IntegerField(default=0)),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Agency.tbl_busdetails')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_userregister')),
            ],
        ),
    ]
