# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Field(models.Model):
    city_name = models.CharField(max_length=30)
    street_name = models.CharField(max_length=30)
    lat_location = models.FloatField()
    long_location = models.FloatField()
    photos = models.ImageField()
    rating = models.IntegerField()
    def __str__(self):
        return self.city_name

class Region(models.Model):
    country_part = models.CharField(max_length=30)
    def __str__(self):
        return self.country_part
    
class Town(models.Model):
    city_name = models.CharField(max_length=30)
    country_part = models.CharField(max_length=30)
    def __str__(self):
        return self.city_name
