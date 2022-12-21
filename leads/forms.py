from email.policy import default
from django import forms
from django.forms import ModelForm
from .models import lead
# class leadform(forms.Form):
#     first_name = forms.CharField(max_length=100)
#     last_name = forms.CharField(max_length=100)
#     age = forms.IntegerField(default=0)

class leadform(ModelForm):
    class Meta:
        model = lead
        fields = '__all__'
