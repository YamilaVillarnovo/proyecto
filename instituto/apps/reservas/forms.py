from django import forms
from apps.reservas.models import Reservas

class ReservasForm(forms.ModelForm):
    class Meta:
        model = Reservas
        fields = '__all__'