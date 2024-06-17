from django.forms import ModelForm, Textarea

from hunts.models import Hunt

class CreateHuntForm(ModelForm):
    class Meta:
        model = Hunt
        fields = ['date_of_hunt', 'photo_url', 'location', 'total_ducks', 'total_geese', 'bird1', 'notes' ]
        labels = {
            'first_clue': 'First Clue',
        }
        widgets = {
            "notes": Textarea(attrs={"cols": 80, "rows": 20}),
        }
        help_texts = {
            'photo_url': "upload your photo here",
        }