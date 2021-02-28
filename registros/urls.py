from django.conf.urls import url
from .views import RegistrosListView, RegistroCreate

registros_patterns = ([
    url('registrar/', RegistroCreate.as_view(), name="registrar"),
    url('', RegistrosListView.as_view(), name="registros"),
], 'registros')