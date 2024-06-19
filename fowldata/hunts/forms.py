from mapwidgets.widgets import MapboxPointFieldWidget

from django.forms import ModelForm, Textarea

from hunts.models import Hunt

class CreateHuntForm(ModelForm):
    class Meta:
        model = Hunt
        fields = ['date_of_hunt', 'photo_url', 'location', 'total_ducks', 'total_geese', 'bird1', 'notes' ]
        widgets = {
            "notes": Textarea(attrs={"cols": 80, "rows": 20}),
            'location': MapboxPointFieldWidget(),
            'photo_url': "upload your photo here",
        }