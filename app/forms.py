from django import forms
from app.models import *

class Djangoform(forms.Form):
    name=forms.CharField(max_length=50)
    age=forms.IntegerField()
    email=forms.EmailField()
    marks=forms.IntegerField(max_value=100)

class Modelform(forms.ModelForm):
    class Meta:
        model=Profile
        fields='__all__'

