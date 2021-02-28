from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from predios.models import Predios
from django.urls import reverse, reverse_lazy
from .forms import PrediosForm
from .filters import PrediosFilter

# Create your views here.
class PrediosListView(ListView):
    model = Predios

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PrediosFilter(self.request.GET, queryset=self.get_queryset())
        return context

class PrediosCreate(CreateView):
    model = Predios
    form_class = PrediosForm

    def get_success_url(self):
        return reverse('predios:predios')

class PrediosUpdate(UpdateView):
    model = Predios
    fields = ['nombre_Predio', 'num_Matr_Inmob', 'Tipo', 'ced_Catastral','dir_Predio']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('predios:actualizar', args=[self.object.id]) + '?ok'