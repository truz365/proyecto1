from django.urls import path 

from .views import *

app_name = 'biblioteca'

urlpatterns = [
    path('<pk>/update', librosUpdateView.as_view(), name='update-libro'),
    path('create', librosCreateView.as_view(), name='create-libro'),
    path('', LibrosLista.as_view(), name='list-libros'),
    path('buscar/', buscar_libros, name='buscar_libros'),
]
