from django.db import models
from Agency.models import *
from Guest.models import *
# Create your models here.
class tbl_packagebooking(models.Model):
    pbooking_date=models.DateField(auto_now=True)
    pbooking_status=models.IntegerField(default=0)
    pbooking_loc=models.CharField(max_length=70,null=True)
    package=models.ForeignKey(tbl_packagedetails,on_delete=models.CASCADE)
    user=models.ForeignKey(tbl_userRegister,on_delete=models.CASCADE)
    pbooking_fordate=models.DateField()
    ppassengers=models.IntegerField(null=True)
    pbooking_amount=models.CharField(max_length=30,null=True)

class tbl_busbooking(models.Model):
    bbooking_date=models.DateField(auto_now=True)
    start_date=models.DateField()
    end_date=models.DateField()
    from_loc=models.CharField(max_length=50,null=True)
    to_loc=models.CharField(max_length=50)
    passengers=models.IntegerField()
    bbooking_amount=models.CharField(max_length=30,default=0)
    btotal_amount=models.CharField(max_length=30,default=0)
    purpose=models.CharField(max_length=30,default=0)
    bbooking_status=models.IntegerField(default=0)
    bus=models.ForeignKey(tbl_busdetails,on_delete=models.CASCADE)
    user=models.ForeignKey(tbl_userRegister,on_delete=models.CASCADE)
    

class tbl_payement(models.Model):
    pbooking=models.ForeignKey(tbl_packagebooking,on_delete=models.CASCADE,null=True)
    bbooking=models.ForeignKey(tbl_busbooking,on_delete=models.CASCADE,null=True)
    payement_amount=models.CharField(max_length=30)
    host_profit=models.CharField(max_length=30)
    agency_profit=models.CharField(max_length=30)
    payement_date=models.DateField(auto_now=True)



class Chat(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    from_user = models.ForeignKey(
        tbl_userRegister, on_delete=models.SET_NULL, default=False, null=True, related_name="from_user")
    to_user = models.ForeignKey(
        tbl_userRegister, on_delete=models.SET_NULL, default=False, null=True, related_name="to_user")
    from_agency = models.ForeignKey(
        tbl_agencyRegister, on_delete=models.SET_NULL, default=False, null=True, related_name="from_agency")
    to_agency = models.ForeignKey(
        tbl_agencyRegister, on_delete=models.SET_NULL, default=False, null=True, related_name="to_agency")
    content = models.TextField()
    is_read=models.BooleanField(default=False)


class tbl_complaint(models.Model):
    name=models.CharField(max_length=100,null=True)
    email=models.EmailField(null=True)
    complaint_title=models.CharField(max_length=50)
    complaint_content=models.TextField()
    complaint_status=models.IntegerField(default=0)
    complaint_reply=models.TextField(null=True)
    complaint_date=models.DateField(auto_now=True)
    user=models.ForeignKey(tbl_userRegister,on_delete=models.CASCADE,null=True)
    agency=models.ForeignKey(tbl_agencyRegister,on_delete=models.CASCADE,null=True)
    package=models.ForeignKey(tbl_packagedetails,on_delete=models.CASCADE,null=True)
    bus=models.ForeignKey(tbl_busdetails,on_delete=models.CASCADE,null=True)



class tbl_rating(models.Model):
    rating_data=models.IntegerField()
    user_name=models.CharField(max_length=500)
    user_review=models.CharField(max_length=500)
    package=models.ForeignKey(tbl_packagedetails,on_delete=models.CASCADE)
    datetime=models.DateTimeField(auto_now_add=True)
