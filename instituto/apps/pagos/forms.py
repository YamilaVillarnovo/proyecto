from django import forms
from apps.pagos.models import Pagos

class PagosForm(forms.ModelForm):
    class Meta:
        model = Pagos
        fields = '__all__'