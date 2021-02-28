from django.conf.urls import url
from predios.views import PrediosListView, PrediosCreate, PrediosUpdate

predios_patterns = ([
    url('registrar/', PrediosCreate.as_view(), name="registrar"),
    url('actualizar/(?P<pk>[0-9]+)/$', PrediosUpdate.as_view(), name="actualizar"),
    url('', PrediosListView.as_view(), name="predios"),
], 'predios')