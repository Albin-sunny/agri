from django.db import models
from Admin.models import *
from Guest.models import *
from Merchant.models import *




# Create your models here.



   
    
   




class tbl_land(models.Model):
    land_file = models.FileField(upload_to='Assets/File/land')
    land_details = models.CharField(max_length=200)
    land_proof = models.FileField(upload_to='Assets/File/land')
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE, null=True)

class tbl_request(models.Model):
    request_date=models.DateField(auto_now_add=True)
    request_status=models.IntegerField(default=0)
    land=models.ForeignKey(tbl_land,on_delete=models.CASCADE, null=True, blank=True)
    coordinator=models.ForeignKey(tbl_coordinator, on_delete=models.CASCADE, null=True, blank=True)
    


class tbl_booking(models.Model):
    booking_date=models.DateField(auto_now_add=True)
    booking_amount=models.CharField(max_length=200)
    user=models.ForeignKey(tbl_user, on_delete=models.CASCADE, null=True, blank=True)
    booking_status=models.IntegerField(default=0)


class tbl_cart(models.Model):
    cart_qty=models.IntegerField(default=1)    
    booking=models.ForeignKey(tbl_booking, on_delete=models.CASCADE, null=True, blank=True)
    cart_status=models.IntegerField(default=0)
    product=models.ForeignKey(tbl_product, on_delete=models.CASCADE, null=True, blank=True)

class tbl_rating(models.Model):
    rating_data=models.IntegerField(default=0)
    rating_datetime=models.DateField(auto_now_add=True)
    rating_review=models.CharField(max_length=100)
    product=models.ForeignKey(tbl_product,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    coordinator=models.ForeignKey(tbl_coordinator,on_delete=models.CASCADE,null=True)



class tbl_feedback(models.Model):
    feedback_content=models.CharField(max_length=200)
    feedback_date=models.DateField(auto_now_add=True)
    user=models.ForeignKey(tbl_user, on_delete=models.CASCADE, null=True, blank=True)

