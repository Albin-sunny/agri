from django.db import models
from Coordinator.models import *

# Create your models here.




class tbl_chat(models.Model):
    chat_content = models.CharField(max_length=500)
    chat_time = models.DateTimeField()
    chat_file = models.FileField(upload_to='ChatFiles/')
    user_from = models.ForeignKey(tbl_user,on_delete=models.CASCADE,related_name="user_from", null=True)
    user_to = models.ForeignKey(tbl_user,on_delete=models.CASCADE,related_name="user_to", null=True)
    plantsman_from = models.ForeignKey(tbl_plantsman,on_delete=models.CASCADE,related_name="plantsman_from", null=True)
    plantsman_to = models.ForeignKey(tbl_plantsman,on_delete=models.CASCADE,related_name="plantsman_to", null=True)


class tbl_prequest(models.Model):  
      request_date=models.DateField(auto_now_add=True)
      discription=models.CharField(max_length=200)
      Merchant=models.ForeignKey(tbl_merchant, on_delete=models.CASCADE, null=True, blank=True)
      request_status=models.IntegerField(default=0)
      request_amount=models.IntegerField(default=0)
      User_amount=models.CharField(max_length=200,null=True)
      assign=models.ForeignKey(tbl_assign, on_delete=models.CASCADE, null=True, blank=True)
