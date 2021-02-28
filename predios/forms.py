from django import forms
from django.forms import ModelForm
from .models import Predios

class PrediosForm(ModelForm):
    
    class Meta:
        model = Predios
        fields = {
            'num_Matr_Inmob',
            'Tipo',
            'ced_Catastral',
            'dir_Predio',
            'nombre_Predio'
        }