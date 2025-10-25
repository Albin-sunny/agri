from django.db import models
from Admin.models import *

# Create your models here.
class tbl_user(models.Model):
    user_name=models.CharField(max_length=60)
    user_email=models.CharField(max_length=60)
    user_contact=models.CharField(max_length=60)
    user_address=models.CharField(max_length=60)
    user_photo=models.FileField(upload_to='Assets/File/User')
    # place=models.ForeignKey(tbl_place, on_delete=models.CASCADE)
    location = models.ForeignKey(tbl_location, on_delete=models.CASCADE)
    user_password=models.CharField(max_length=60)
   

class tbl_coordinator(models.Model):
    coordinator_name=models.CharField(max_length=255)
    coordinator_email=models.EmailField(unique=True)
    coordinator_contact=models.CharField(max_length=15)
    coordinator_address=models.TextField()
    coordinator_photo = models.FileField(upload_to='Assets/File/Coordinator')
    coordinator_proof = models.FileField(upload_to='Assets/File/Coordinator')
    coordinator_password=models.CharField(max_length=255)
    location = models.ForeignKey(tbl_location, on_delete=models.CASCADE, null=True, blank=True)
    coordinator_status=models.IntegerField(default=0)




class tbl_merchant(models.Model):
    merchant_name=models.CharField(max_length=255)
    merchant_email=models.EmailField(unique=True)
    merchant_contact=models.CharField(max_length=15)
    merchant_address=models.TextField()
    merchant_photo=models.FileField(upload_to='Assets/File/Merchant')
    merchant_proof = models.FileField(upload_to='Assets/File/Merchant')
    merchant_password=models.CharField(max_length=255)
    location = models.ForeignKey(tbl_location, on_delete=models.CASCADE, null=True, blank=True)
    merchant_status=models.IntegerField(default=0)


