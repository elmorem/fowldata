from django import forms
from django.forms import ModelForm

from hunts.models import Hunt

class CreateHuntForm(ModelForm):
    class Meta:
        model = Hunt
        fields = "__all__"
        # ['date_of_hunt',  'latitude', 'longitude', 'total_ducks', 'total_geese', 'bird1', 'notes' ]
        # widgets = {
        #     'date_of_hunt': forms.SelectDateWidget(),
        #    'latitude': forms.NumberInput(),
        #    'longitude': forms.NumberInput(),
        #     'total_ducks': forms.NumberInput(),
        #     'total_geese': forms.NumberInput(),
        #     'bird1': forms.Select(choices=Hunt.WATERFOWL_CHOICES),
        #     "notes": forms.Textarea(attrs={"cols": 80, "rows": 20}),
        # }