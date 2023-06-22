from django import forms

from .models import Marker

class marker_Form(forms.ModelForm):

    class Meta:
        model = Marker
        fields = ('latitude', 'longitude',)