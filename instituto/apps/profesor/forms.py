from django import forms
from apps.profesor.models import profesor

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = profesor
        fields = '__all__'