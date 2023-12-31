# Generated by Django 4.2.1 on 2023-06-10 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_rename_pbooing_amount_tbl_packagebooking_pbooking_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_payement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payement_amount', models.CharField(max_length=30)),
                ('admin_profit', models.CharField(max_length=30)),
                ('agency_profit', models.CharField(max_length=30)),
                ('payement_date', models.DateField(auto_now=True)),
                ('pbooking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.tbl_packagebooking')),
            ],
        ),
    ]
