from django.db import models
from django.contrib.auth.models import User

class PassWordModel(models.Model):
    PassWord1=models.CharField(max_length=120)
    PassWord2=models.CharField(max_length=120)
    user=models.ForeignKey(User,on_delete=models.CASCADE)


class OrganizationModel(models.Model):
    Person_First_name=models.CharField(max_length=120)
    Person_Last_name = models.CharField(max_length=120)
    Person_Age=models.PositiveIntegerField()
    Person_Gender=models.CharField(max_length=120)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="organization")




