# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from models import *

admin.site.register(Profile)
admin.site.register(Feedback)
admin.site.register(Locations)
admin.site.register(LocationTypes)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Area)
admin.site.register(State_City_Area)
admin.site.register(Notifications)