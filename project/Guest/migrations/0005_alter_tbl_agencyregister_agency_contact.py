# Generated by Django 4.2.1 on 2023-06-01 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0004_tbl_agencyregister_agency_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_agencyregister',
            name='agency_contact',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
