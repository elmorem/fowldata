from django.forms import ModelForm

from hunts.models import Hunt

class CreateHuntForm(ModelForm):
    class Meta:
        model = Hunt
        fields = ['user', 'date_of_hunt',  'total_ducks', 'total_geese', 'location', 'latitude', 'longitude', 'weather_id']   