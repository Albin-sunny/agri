from django.db import models
from Guest.models import *

# Create your models here.




class tbl_product(models.Model):
    product_name=models.CharField(max_length=255)
    product_photo=models.FileField(upload_to='Assets/File/Merchant')
    product_price=models.CharField(max_length=255)
    product_description=models.CharField(max_length=255)
    merchant=models.ForeignKey(tbl_merchant, on_delete=models.CASCADE, null=True, blank=True)




class tbl_addstock(models.Model):
    product=models.ForeignKey(tbl_product, on_delete=models.CASCADE, null=True, blank=True)
    stock_date=models.DateField(auto_now_add=True)
    stock_qty=models.CharField(max_length=200)
