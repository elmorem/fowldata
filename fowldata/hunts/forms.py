from django.forms import ModelForm

from hunts.models import Hunt

class CreateHuntForm(ModelForm):
    class Meta:
        model = Hunt
        fields = "__all__"
        labels = {
            'first_clue': 'First Clue',
        }