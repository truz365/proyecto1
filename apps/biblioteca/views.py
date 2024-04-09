from django.shortcuts import render
from .models import Libro
from .forms import BusquedaLibroForm

# Create your views here.

# import generic UpdateView 
from django.views.generic.edit import (
    UpdateView, CreateView, 
    )
from django.views.generic.list import (
    ListView
    )
                        

from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from apps.users.helpers import *

class librosUpdateView(StaffRequiredMixin,UpdateView):
    model = Libro
    fields = ['Autor','titulo','genero','ano_edicion','isbn','editorial']
    template_name = 'biblioteca/updatelibro.html'
    success_url = "/"
    login_url = reverse_lazy('users:login')


class librosCreateView(StaffRequiredMixin,CreateView):
    model = Libro
    fields = ['Autor','titulo','genero','ano_edicion','isbn','editorial']
    template_name = 'biblioteca/createlibro.html'
    success_url = "/"
    login_url = reverse_lazy('users:login')

 
class LibrosLista(StaffRequiredMixin,ListView):
    # specify the model for list view
    model = Libro
    template_name = 'biblioteca/listalibro.html'
    login_url = reverse_lazy('users:login')

def buscar_libros(request):
    if request.method == 'POST':
        form = BusquedaLibroForm(request.POST)
        if form.is_valid():
            termino_busqueda = form.cleaned_data['termino_busqueda']
            libros = Libro.objects.filter(titulo__icontains=termino_busqueda)
            return render(request, 'biblioteca/resultado_busqueda.html', {'libros': libros})
    else:
        form = BusquedaLibroForm()
    return render(request, 'biblioteca/buscarlibro.html', {'form': form})
