# Generated by Django 4.2.1 on 2023-05-30 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0004_tbl_subcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_userRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('user_contact', models.CharField(max_length=20)),
                ('user_email', models.EmailField(max_length=254, unique=True)),
                ('user_gender', models.CharField(max_length=20)),
                ('user_address', models.TextField()),
                ('user_photo', models.FileField(upload_to='userdocs/')),
                ('user_password', models.CharField(max_length=70, unique=True)),
                ('place_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Admin.tbl_place')),
            ],
        ),
    ]