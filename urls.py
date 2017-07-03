from django.conf.urls import url
from django.contrib import admin
import views

app_name="slickApp"

urlpatterns=[
    url(r'test1',views.test1),
    url(r'temples/([0-9])$',views.temples,name="temples"),
    url(r'temples/rating/$',views.templerating,name="location"),
    url(r'reg/$', views.reg_form)
]
