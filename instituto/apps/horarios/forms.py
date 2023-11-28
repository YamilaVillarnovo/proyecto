from django import forms
from apps.horarios.models import Horarios

class HorariosForm(forms.ModelForm):
    class Meta:
        model = Horarios
        fields = '__all__'