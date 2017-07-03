# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

class Feedback(models.Model):
      Userid = models.IntegerField()
      feedback = models.CharField(max_length = 256)
      created_date = models.DateTimeField(timezone.now)

      def __str__(self):
        return self.name

class LocationTypes(models.Model):
      Location_id = models.IntegerField()
      Location_type = models.CharField(max_length = 256)
      def __str__(self):
        return self.name

class State(models.Model):
      State_id = models.IntegerField(null= True)
      State_name = models.CharField(max_length= 256)

      def __str__(self):
        return self.name

class City(models.Model):
      City_id = models.IntegerField(default=None)
      City_Name = models.CharField(max_length = 256)

      def __str__(self):
        return self.name

class Area(models.Model):
      Area_id = models.IntegerField(default=None)
      Area_name = models.CharField(max_length = 256)

      def __str__(self):
        return self.name

class State_City_Area(models.Model):
      State_id = models.IntegerField()
      City_id = models.IntegerField()
      Area_id = models.IntegerField()

      def __str__(self):
        return self.name

class Notifications(models.Model):
      City_State_areaid = models.ForeignKey(State_City_Area)
      Event_name = models.CharField(max_length = 256)
      Date_Time = models.DateTimeField(default = timezone.now)

      def __str__(self):
        return self.name

class Locations(models.Model):
      Name = models.CharField(max_length = 256)
      Address = models.CharField(max_length = 256)
      Landmark = models.CharField(max_length = 256)
      City_State_areaid = models.ForeignKey(State_City_Area)
      Rating = models.IntegerField()
      Location_typeid = models.IntegerField()

      def __str__(self):
        return self.name

class Profile(models.Model):
      Userid = models.CharField(max_length=256, null= True, blank=True, default=None)
      fname = models.CharField(max_length=256, null= True, blank=True, default=None)
      mname = models.CharField(max_length=256, null= True, blank=True, default=None)
      lname = models.CharField(max_length=256, null= True, blank=True, default=None)
      City_State_areaid = models.ForeignKey(State_City_Area)
      PhoneNumber =  models.CharField(max_length=12)
      Email = models.EmailField(default=None)

      @receiver(post_save, sender = Userid)
      def create_user_profile(sender, instance, created, **kwargs):
          if created:
              Profile.objects.create(user = instance)

      @receiver(post_save, sender = Userid)
      def save_user_profile(sender, instance, **kwargs):
          instance.Profile.save()

      def __str__(self):
        return self.name