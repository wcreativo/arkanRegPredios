import django_filters
from .models import Propietarios

class PropietariosFilter(django_filters.FilterSet):

    class Meta:
        model = Propietarios
        fields = {
            'nom_Prop':['icontains'],
            'ced_Prop':['icontains'],
        }

