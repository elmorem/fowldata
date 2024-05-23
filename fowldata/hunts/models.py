from django.db import models

from accounts.models import MyUser

class HuntManager(models.Manager):
    pass

class Hunt(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    date_of_hunt = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)
    total_ducks = models.IntegerField(default=0, help_text=" Total number of ducks taken during hunt.")
    total_geese = models.IntegerField(default=0, help_text=" Total number of geese taken during hunt.")
    photo= models.ImageField(blank=True,)