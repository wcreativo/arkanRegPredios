from django import forms
from django.forms import ModelForm
from .models import Registros


class RegistrosForm(ModelForm):
    
    class Meta:
        model = Registros
        fields = {
            'predio',
            'propietarios'
        }





