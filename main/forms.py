from  django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from . models import Users_info

class form_info(ModelForm):
    class Meta:
        model = Users_info
        feild = ['acc_no','balance']