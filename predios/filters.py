import django_filters
from .models import Predios

class PrediosFilter(django_filters.FilterSet):


    class Meta:
        model = Predios
        fields = {
            'nombre_Predio': ['icontains'],
            'num_Matr_Inmob': ['icontains'],
            'Tipo': ['icontains'],
            'ced_Catastral': ['icontains'],
            'dir_Predio': ['icontains'],
        }