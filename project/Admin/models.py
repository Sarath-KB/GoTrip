from django.db import models

# Create your models here.
class tbl_district(models.Model):
    district_name=models.CharField(max_length=50)


class tbl_packagetype(models.Model):
    packagetype_name=models.CharField(max_length=70)


class tbl_place(models.Model):
    place_name=models.CharField(max_length=40)
    district=models.ForeignKey(tbl_district,on_delete=models.CASCADE)

    
