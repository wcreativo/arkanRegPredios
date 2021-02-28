from django.conf.urls import url
from propietarios.views import PropietariosListView, PropietariosCreate, PropietariosUpdate

propietarios_patterns = ([
    url('registrar/', PropietariosCreate.as_view(), name="registrar"),
    url('actualizar/(?P<pk>[0-9]+)/$', PropietariosUpdate.as_view(), name="actualizar"),
    url('', PropietariosListView.as_view(), name="propietarios"),
], 'propietarios')