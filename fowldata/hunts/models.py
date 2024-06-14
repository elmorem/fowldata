from django.contrib.gis.db import models as gis_models
from django.contrib.gis.geos import Point
from django.db import models

from accounts.models import MyUser

class HuntManager(models.Manager):
    def create_hunt(self, location):
        pass



class Hunt(models.Model):
    WATERFOWL_CHOICES = [
        ('Dabblers',(
            ('American Black Duck','American Black Duck'),
            ('American Wigeon', 'American Wigeon'),
            ('Blue-winged Teal','Blue-winged Teal'),
            ('Cinnamon Teal', 'Cinnamon Teal'),
            ('Eurasian Wigeon', 'Eurasian Wigeon'),
            ('Gadwall','Gadwall'),
            ('Green-winged Teal', 'Green-winged Teal'),
            ('Mallard', 'Mallard'),
            ('Mottled Duck', 'Mottled Duck'),
            ('Northern Pintail', 'Northern Pintail'),
            ('Northern Shoveler', 'Northern Shoveler'),
            ('Wood Duck', 'Wood Duck'),
    )
        ),
        ('Divers',(
            ('Barrows Goldeneye', 'Barrows Goldeneye'),
            ('Black Scoter','Black Scoter'),
            ('Bufflehead', 'Bufflehead'),
            ('Canvasback', 'Canvasback'),
            ('Common Eider', 'Common Eider'),
            ('Common Goldeneye', 'Common Goldeneye'),
            ('Common Merganser', 'Common Merganser'),
            ('Greater Scaup', 'Greater Scaup'),
            ('Harlequin Duck', 'Harlequin Duck'),
            ('Hooded Merganser','Hooded Merganser'),
            ('King Eider', 'King Eider'),
            ('Lesser Scaup', 'Lesser Scaup'),
            ('Long-Tailed Duck', 'Long-Tailed Duck'),
            ('Red-breasted Merganser', 'Red-breasted Merganser'),
            ('Redhead', 'Redhead'),
            ('Ring-necked Duck', 'Ring-necked Duck'),
            ('Spectacled Eider', 'Spectacled Eider'),
            ('Stellers Eider', 'Stellers Eider'),
            ('Surf Scoter', 'Surf Scoter'),
        )
        ),
        ('Geese',(
            ('Barnacle Goose', 'Barnacle Goose'),
            ('Brant', 'Brant'),
            ('Cackling Goose', 'Cackling Goose'),
            ('Canada Goose', 'Canada Goose'),
            ('Emperor Goose', 'Emperor Goose'),
            ('Hawaiian Nene Goose', 'Hawaiian Nene Goose'),
            ('Ross Goose', 'Ross Goose'),
            ('Snow Goose', 'Snow Goose'),
            ('White-fronted Goose', 'White-fronted Goose'),
        )
        )
    ]
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    date_of_hunt = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)
    photo_url = models.URLField() 
    location = gis_models.PointField(geography=True, default=Point(0.0, 0.0)) 
    latitude = models.FloatField()
    longitude = models.FloatField()
    weather_id = models.IntegerField(null=True, blank=True)
    total_ducks = models.IntegerField(default=0, help_text=" Total number of ducks taken during hunt.")
    total_geese = models.IntegerField(default=0, help_text=" Total number of geese taken during hunt.")
    notes = models.TextField(blank=True)
    bird1 = models.CharField(max_length=100, choices=WATERFOWL_CHOICES, blank=True)
    bird2 = models.CharField(max_length=100, choices=WATERFOWL_CHOICES, blank=True)
    bird3 = models.CharField(max_length=100, choices=WATERFOWL_CHOICES, blank=True)
    bird4 = models.CharField(max_length=100, choices=WATERFOWL_CHOICES, blank=True)
    bird5 = models.CharField(max_length=100, choices=WATERFOWL_CHOICES, blank=True)
    bird6 = models.CharField(max_length=100, choices=WATERFOWL_CHOICES, blank=True)
    bird7 = models.CharField(max_length=100, choices=WATERFOWL_CHOICES, blank=True)
    bird8 = models.CharField(max_length=100, choices=WATERFOWL_CHOICES, blank=True)
    bird9 = models.CharField(max_length=100, choices=WATERFOWL_CHOICES, blank=True)
    bird10 = models.CharField(max_length=100, choices=WATERFOWL_CHOICES, blank=True)
    bird11 = models.CharField(max_length=100, choices=WATERFOWL_CHOICES, blank=True)
    bird12 = models.CharField(max_length=100, choices=WATERFOWL_CHOICES, blank=True)
    bird13 = models.CharField(max_length=100, choices=WATERFOWL_CHOICES, blank=True)
    bird14 = models.CharField(max_length=100, choices=WATERFOWL_CHOICES, blank=True)
    bird15 = models.CharField(max_length=100, choices=WATERFOWL_CHOICES, blank=True)
    bird16 = models.CharField(max_length=100, choices=WATERFOWL_CHOICES, blank=True)
    bird17 = models.CharField(max_length=100, choices=WATERFOWL_CHOICES, blank=True)
    bird18 = models.CharField(max_length=100, choices=WATERFOWL_CHOICES, blank=True)
    bird19 = models.CharField(max_length=100, choices=WATERFOWL_CHOICES, blank=True)
    bird20 = models.CharField(max_length=100, choices=WATERFOWL_CHOICES, blank=True)
    bird21 = models.CharField(max_length=100, choices=WATERFOWL_CHOICES, blank=True)
    bird22 = models.CharField(max_length=100, choices=WATERFOWL_CHOICES, blank=True)
    bird23 = models.CharField(max_length=100, choices=WATERFOWL_CHOICES, blank=True)
    bird24 = models.CharField(max_length=100, choices=WATERFOWL_CHOICES, blank=True)
    bird25 = models.CharField(max_length=100, choices=WATERFOWL_CHOICES, blank=True)
    bird26 = models.CharField(max_length=100, choices=WATERFOWL_CHOICES, blank=True)
    bird27 = models.CharField(max_length=100, choices=WATERFOWL_CHOICES, blank=True)
    bird28 = models.CharField(max_length=100, choices=WATERFOWL_CHOICES, blank=True)
    bird29 = models.CharField(max_length=100, choices=WATERFOWL_CHOICES, blank=True)
    bird30 = models.CharField(max_length=100, choices=WATERFOWL_CHOICES, blank=True)
    bird31 = models.CharField(max_length=100, choices=WATERFOWL_CHOICES, blank=True)
    bird32 = models.CharField(max_length=100, choices=WATERFOWL_CHOICES, blank=True)
    bird33 = models.CharField(max_length=100, choices=WATERFOWL_CHOICES, blank=True)
    bird34 = models.CharField(max_length=100, choices=WATERFOWL_CHOICES, blank=True)
    bird35 = models.CharField(max_length=100, choices=WATERFOWL_CHOICES, blank=True)
    bird36 = models.CharField(max_length=100, choices=WATERFOWL_CHOICES, blank=True)
    bird37 = models.CharField(max_length=100, choices=WATERFOWL_CHOICES, blank=True)
    bird38 = models.CharField(max_length=100, choices=WATERFOWL_CHOICES, blank=True)
    bird39 = models.CharField(max_length=100, choices=WATERFOWL_CHOICES, blank=True)
    bird40 = models.CharField(max_length=100, choices=WATERFOWL_CHOICES, blank=True)
    bird41 = models.CharField(max_length=100, choices=WATERFOWL_CHOICES, blank=True)
    bird42 = models.CharField(max_length=100, choices=WATERFOWL_CHOICES, blank=True)
    bird43 = models.CharField(max_length=100, choices=WATERFOWL_CHOICES, blank=True)
    bird44 = models.CharField(max_length=100, choices=WATERFOWL_CHOICES, blank=True)
    bird45 = models.CharField(max_length=100, choices=WATERFOWL_CHOICES, blank=True)
    bird46 = models.CharField(max_length=100, choices=WATERFOWL_CHOICES, blank=True)
    bird47 = models.CharField(max_length=100, choices=WATERFOWL_CHOICES, blank=True)
    bird48 = models.CharField(max_length=100, choices=WATERFOWL_CHOICES, blank=True)
    bird49 = models.CharField(max_length=100, choices=WATERFOWL_CHOICES, blank=True)
    bird50 = models.CharField(max_length=100, choices=WATERFOWL_CHOICES, blank=True)




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
