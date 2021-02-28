import django_filters
from .models import Registros

class RegistroFilter(django_filters.FilterSet):
    nom_Prop = django_filters.CharFilter(field_name='propietarios', lookup_expr='nom_Prop')
    ced_Prop = django_filters.CharFilter(field_name='propietarios', lookup_expr='ced_Prop')
    ced_Catastral = django_filters.CharFilter(field_name='predio', lookup_expr='ced_Catastral')
    dir_Predio = django_filters.CharFilter(field_name='predio', lookup_expr='dir_Predio')
    nombre_Predio = django_filters.CharFilter(field_name='predio', lookup_expr='nombre_Predio')

    class Meta:
        model = Registros
        fields = {
            'nom_Prop':['icontains'],
            'ced_Prop':['icontains'],
            'ced_Catastral':['icontains'],
            'dir_Predio':['icontains'],
            'nombre_Predio':['icontains'],
        }

