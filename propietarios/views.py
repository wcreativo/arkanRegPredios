from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from .models import Propietarios
from .filters import PropietariosFilter
from .forms import PropietariosForm

# Create your views here.

class PropietariosListView(ListView):
    model = Propietarios

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PropietariosFilter(self.request.GET, queryset=self.get_queryset())
        return context

class PropietariosCreate(CreateView):
    model = Propietarios
    form_class = PropietariosForm

    def get_success_url(self):
        return reverse('propietarios:propietarios')

class PropietariosUpdate(UpdateView):
    model = Propietarios
    fields = ['nom_Prop', 'ced_Prop']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('propietarios:actualizar', args=[self.object.id]) + '?ok'