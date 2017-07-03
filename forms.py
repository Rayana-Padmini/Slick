from django import forms
from models import *

class regForm(forms.Form):
    fname = forms.CharField(max_length=100)
    mname = forms.CharField(max_length=100)
    Email = forms.EmailField()
    lname = forms.CharField(max_length=100)
    PhoneNumber = forms.IntegerField()
    Userid = forms.CharField(max_length=100)

    #class Meta:
     #   model = Profile
      #  fields = {'fname','mname','lname','Email','PhoneNumber','Userid'}

