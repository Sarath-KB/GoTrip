# Generated by Django 4.2.1 on 2023-07-03 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0009_tbl_admin'),
        ('Agency', '0018_remove_tbl_busdetails_bus_rate'),
        ('User', '0013_rename_admin_profit_tbl_payement_host_profit_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(null=True)),
                ('rating', models.IntegerField(null=True)),
                ('bus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Agency.tbl_busdetails')),
                ('package', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Agency.tbl_packagedetails')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Guest.tbl_userregister')),
            ],
        ),
    ]
