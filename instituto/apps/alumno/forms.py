from django import forms
from apps.alumno.models import alumnoTable

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = alumnoTable
        fields = '__all__'
