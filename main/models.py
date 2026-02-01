from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Users_info(models.Model):
    acc_no = models.IntegerField(default=0)
    balance = models.IntegerField(default=0)
    user = models.ForeignKey(User,on_delete=models.CASCADE)