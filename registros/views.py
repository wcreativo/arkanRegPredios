from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Registros
from .filters import RegistroFilter
from django.urls import reverse, reverse_lazy
from registros.forms import RegistrosForm


# Create your views here.
class RegistrosListView(ListView):
    model = Registros

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = RegistroFilter(self.request.GET, queryset=self.get_queryset())
        return context


class RegistroCreate(CreateView):
    model = Registros
    form_class = RegistrosForm


    def get_success_url(self):
        return reverse('registros:registros')

   
