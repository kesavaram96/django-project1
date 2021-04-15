from django.db import models

# Create your models here.
class user(models.Model):
    UId=models.IntegerField()
    UName=models.CharField(max_length=30)
    EMail=models.EmailField()
    password=models.CharField(max_length=10)
    