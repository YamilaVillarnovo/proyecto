from django import forms
from apps.rutina.models import Rutina

class RutinaForm(forms.ModelForm):
    class Meta:
        model = Rutina
        fields = '__all__'