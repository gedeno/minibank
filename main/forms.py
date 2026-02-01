from django.forms import ModelForm
from .models import Users_info

class form_info(ModelForm):
    class Meta:
        model = Users_info
        fields = ['name','acc_no']