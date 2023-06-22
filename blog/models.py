from django.db import models
from django.db import models
from django.contrib.gis.db import models

class Marker(models.Model):
    latitude = models.CharField(max_length=40)
    longitude = models.CharField(max_length=40)

class Node(models.Model):
    point = models.PointField()

# Create your models here.
