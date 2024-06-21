from django import forms
from django.forms import ModelForm


from hunts.models import Hunt
class CreateHuntForm(ModelForm):
    class Meta:
        model = Hunt
        fields = ['date_of_hunt', 'photo_url', 'location', 
                  'total_ducks', 'total_geese', 'bird1', 'bird2',
                  'notes' ]
