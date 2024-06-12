from django.contrib.gis.db import models as gis_models
from django.contrib.gis.geos import Point
from django.db import models

from accounts.models import MyUser

class HuntManager(models.Manager):
    def create_hunt(self, location):
        pass



class Hunt(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    date_of_hunt = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)
    total_ducks = models.IntegerField(default=0, help_text=" Total number of ducks taken during hunt.")
    total_geese = models.IntegerField(default=0, help_text=" Total number of geese taken during hunt.")
    photo_url = models.URLField() 
    location = gis_models.PointField(geography=True, default=Point(0.0, 0.0)) 
    latitude = models.FloatField()
    longitude = models.FloatField()
    weather_id = models.IntegerField(null=True, blank=True)


class WeatherManager(models.Manager):
    pass

class Weather (models.Model):
    weatherID = models.BigAutoField(primary_key=True)
    date = models.DateField()
    tempmax = models.FloatField()
    tempmin = models.FloatField()
    temp = models.FloatField()
    dew = models.FloatField()
    humidity = models.FloatField()
    precip = models.FloatField()
    precipprob =models.FloatField()
    precipcover = models.FloatField()
    preciptype = models.CharField(max_length=100)
    windgust = models.FloatField()
    windspeed = models.FloatField()
    winddir = models.FloatField()
    sunrise = models.CharField(max_length=100)
    sunset = models.CharField(max_length=100)


class LocationManager(models.Manager):
    pass

class Location(models.Model):
    lat_long = gis_models.PointField(geography=True, default=Point(0.0, 0.0))
    latitude = models.FloatField()
    longitude = models.FloatField()
    date_added = models.DateTimeField(auto_now_add=True)
    