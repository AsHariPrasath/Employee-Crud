from django.db import models


# Create your models here.

class emp(models.Model):
    fullname=models.CharField(max_length=20)
    contactno=models.IntegerField()
    emailid=models.CharField(max_length=25)
    dateofbirth=models.DateField()
    gender=models.CharField(max_length=10)
    jobrole=models.CharField(max_length=25)
    address=models.CharField(max_length=100)

