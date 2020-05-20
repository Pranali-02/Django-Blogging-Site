from django.db import models
from datetime import datetime

# Create your models here.
class blogtable(models.Model):
    Title=models.CharField(max_length=200,default='')
    Description=models.CharField(max_length=9000)
    Image=models.FileField(upload_to='image/',default='')
    Author=models.CharField(max_length=50,default='')
    upload_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Title
