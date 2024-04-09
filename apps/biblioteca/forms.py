
from django import forms

class BusquedaLibroForm(forms.Form):
    termino_busqueda = forms.CharField(label='Buscar libros', max_length=100)
