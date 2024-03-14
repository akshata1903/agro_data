from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Crop(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    location = models.TextField(max_length=60, blank=True)
    fieldcropid = models.TextField(max_length=60, blank=True)
    croptype = models.TextField(max_length=60, blank=True)
    cropvariety = models.TextField(max_length=60, blank=True)
    name = models.TextField(max_length=60, blank=True)
    expecyieldpeh = models.TextField(max_length=60, blank=True)
    avgplanthei = models.TextField(max_length=60, blank=True)
    expecperi = models.TextField(max_length=60, blank=True)

class Plot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=60, blank=True)
    field = models.CharField(max_length=60, blank=True)
    farm = models.CharField(max_length=60, blank=True)
    farmer = models.CharField(max_length=60, blank=True)
    plot = models.CharField(max_length=60, blank=True)
    rows = models.CharField(max_length=60, blank=True)
    columns = models.CharField(max_length=60, blank=True)
    plants = models.CharField(max_length=60, blank=True)

class Soil(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=60, blank=True)
    dailyweat = models.CharField(max_length=60, blank=True)
    mintemp = models.CharField(max_length=60, blank=True)
    maxtemp = models.CharField(max_length=60, blank=True)
    windspeed = models.CharField(max_length=60, blank=True)
    humidity = models.CharField(max_length=60, blank=True)
    sunshinehrs = models.CharField(max_length=60, blank=True)

class Issue(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=60, blank=True)
    issueid = models.CharField(max_length=60, blank=True)
    solution = models.CharField(max_length=60, blank=True)


class Tool(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=60, blank=True)
    toolid = models.CharField(max_length=60, blank=True)
    toolname = models.CharField(max_length=60, blank=True)
    rate = models.CharField(max_length=60, blank=True)
    # contact = models.CharField(max_length=60, blank=True)