# Generated by Django 4.2.1 on 2023-06-01 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0005_alter_tbl_agencyregister_agency_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_agencyregister',
            name='agency_license',
            field=models.FileField(upload_to='agencydocs/'),
        ),
        migrations.AlterField(
            model_name='tbl_agencyregister',
            name='agency_ownerproof',
            field=models.FileField(upload_to='agencydocs/'),
        ),
    ]
