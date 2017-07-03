# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import *

from django.http import HttpResponse
from django.shortcuts import render
from .forms import regForm
from django.http import Http404
from django.views.generic import ListView
from django.http import HttpResponseRedirect

# Create your views here.

def test1(request):
     return HttpResponse("Hello User")

def temples(request,id):
    tmp = Locations.objects.filter(City_State_areaid=id ,Location_typeid=1);
    rendered=render(request,'slickApp/temples.html',{'temples':tmp})
    return HttpResponse(rendered)

def templerating(request):
    tr = Locations.objects.filter(Location_typeid=1).order_by('Rating');
    rendered=render(request,'slickApp/tmpr.html',{'templerating':tr})
    return HttpResponse(rendered)

def reg_form(request):
    if request.method == 'POST':
        form = regForm(request.POST);
        if form.is_valid():
            Userid = form.cleaned_data['Userid']
            fname = form.cleaned_data['fname']
            mname = form.cleaned_data['mname']
            lname = form.cleaned_data['lname']
            email = form.cleaned_data['Email']
            honeNumber = form.cleaned_data['PhoneNumber']

            return HttpResponseRedirect('/registered/')
    else:
        form = regForm()
    return render(request,'slickApp/registration.html',{'form':form})

#def retloc(request, id):
 #   rtl = City.objects.filter(City_Name);


