# Generated by Django 4.2.1 on 2023-06-01 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0005_tbl_packagetype_tbl_subpackagetype_and_more'),
        ('Guest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbk_agencyRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agency_name', models.CharField(max_length=50)),
                ('agency_ownername', models.CharField(max_length=50)),
                ('agency_email', models.EmailField(max_length=254, unique=True)),
                ('agency_address', models.TextField()),
                ('agency_ownerproof', models.FileField(upload_to='ownerdocs/')),
                ('agency_license', models.FileField(upload_to='ownerdocs/')),
                ('agency_password', models.CharField(max_length=70, unique=True)),
                ('place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Admin.tbl_place')),
            ],
        ),
    ]
