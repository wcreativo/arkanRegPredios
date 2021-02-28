from django import forms
from django.forms import ModelForm
from .models import Propietarios

class PropietariosForm(ModelForm):
    
    class Meta:
        model = Propietarios
        fields = {
            'nom_Prop',
            'ced_Prop',
        }

