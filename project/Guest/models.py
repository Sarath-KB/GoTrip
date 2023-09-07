from django.db import models
from Admin.models import *
# Create your models here.
class tbl_userRegister(models.Model):
    user_name=models.CharField(max_length=50)
    user_contact=models.CharField(max_length=20)
    user_email=models.EmailField(unique=True)
    user_address=models.TextField()
    user_photo=models.FileField(upload_to='userdocs/')
    user_password=models.CharField(max_length=70,unique=True)
    place_id=models.ForeignKey(tbl_place,on_delete=models.SET_NULL,null=True)


class tbl_agencyRegister(models.Model):
    agency_name=models.CharField(max_length=50)
    agency_ownername=models.CharField(max_length=50)
    agency_contact=models.CharField(max_length=15,null=True)
    agency_email=models.EmailField(unique=True)
    agency_address=models.TextField()
    place=models.ForeignKey(tbl_place,on_delete=models.SET_NULL,null=True)
    agency_ownerproof=models.FileField(upload_to='agencydocs/')
    agency_license=models.FileField(upload_to='agencydocs/')
    agency_password=models.CharField(max_length=70,unique=True)
    agency_status=models.IntegerField(default=0)

class tbl_admin(models.Model):
    admin_mail=models.EmailField(unique=True)
    admin_passwd=models.CharField(max_length=20,unique=True)

