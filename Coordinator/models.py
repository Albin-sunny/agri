from django.db import models
from Guest.models import *
from User.models import *
from Admin.models import *
# Create your models here.
class tbl_plantsman(models.Model):
    plantsman_name=models.CharField(max_length=255)
    plantsman_email=models.EmailField(unique=True)
    plantsman_contact=models.CharField(max_length=15)
    plantsman_address=models.TextField()
    plantsman_photo = models.FileField(upload_to='Assets/File/Coordinator')
    plantsman_proof = models.FileField(upload_to='Assets/File/Coordinator')
    plantsman_password=models.CharField(max_length=255)
    location = models.ForeignKey(tbl_location, on_delete=models.CASCADE, null=True)
    coordinator=models.ForeignKey(tbl_coordinator, on_delete=models.CASCADE, null=True)
   

class tbl_assign(models.Model): 
    plantsman = models.ForeignKey(tbl_plantsman, on_delete=models.CASCADE, null=True)
    assign_date=models.DateField(auto_now_add=True)
    assign_status=models.IntegerField(default=0)
    land=models.ForeignKey(tbl_land,on_delete=models.CASCADE, null=True)
     
class tbl_complaint(models.Model): 
    complaint_title=models.CharField(max_length=60)
    complaint_content=models.CharField(max_length=200)
    complaint_date=models.DateField(auto_now_add=True)
    complaint_reply=models.CharField(max_length=60,null=True)
    complaint_status=models.IntegerField(default=0)
    plantsman=models.ForeignKey(tbl_plantsman,on_delete=models.CASCADE, null=True)
    user_id=models.ForeignKey(tbl_user,on_delete=models.CASCADE, null=True)
    product=models.ForeignKey(tbl_product,on_delete=models.CASCADE, null=True)

