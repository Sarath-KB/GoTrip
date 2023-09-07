from django.db import models
from Guest.models import *


# Create your models here.


class tbl_hoteldetails(models.Model):
    hotel_name=models.CharField(max_length=50)
    hotel_address=models.TextField()
    hotel_phno=models.TextField(max_length=20,null=True)
    
    agency=models.ForeignKey(tbl_agencyRegister,on_delete=models.CASCADE)

class tbl_mealdetails(models.Model):
    meal_name=models.CharField(max_length=50)
    
    agency=models.ForeignKey(tbl_agencyRegister,on_delete=models.CASCADE)


class tbl_packagedetails(models.Model):
    
    package_name=models.CharField(max_length=50)
    package_description=models.TextField()
    package_cover=models.FileField(upload_to='packagedocs/')
    package_locations=models.TextField()
    package_days=models.CharField(max_length=20)
    package_nights=models.CharField(max_length=20)
    hotel=models.CharField(max_length=50)
    meal=models.CharField(max_length=50)
    bus=models.CharField(max_length=50,null=True)
    package_persons=models.IntegerField(null=True)
    package_price=models.CharField(max_length=30)
    package_status=models.IntegerField(default=0,null=True)
    agency=models.ForeignKey(tbl_agencyRegister,on_delete=models.CASCADE)


class tbl_dayhighlights(models.Model):
    day_no=models.CharField(max_length=20)
    day_highlights=models.TextField()
    day_image=models.FileField(upload_to='daydocs/',null=True)
    package=models.ForeignKey(tbl_packagedetails,on_delete=models.CASCADE)

class tbl_busdetails(models.Model):
    bus_regno=models.CharField(max_length=40)
    bus_type=models.CharField(max_length=20)
    bus_seatcapacity=models.IntegerField()
    bus_image=models.FileField(upload_to='busdocs/')
    bus_status=models.IntegerField(default=0)
    agency=models.ForeignKey(tbl_agencyRegister,on_delete=models.CASCADE,null=True)
    package=models.ForeignKey(tbl_packagedetails,on_delete=models.SET_NULL,null=True)