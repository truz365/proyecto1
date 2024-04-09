from django.urls import path 
from .views import *
from . import views

app_name = 'users'

urlpatterns = [
    path('login', loginUser.as_view (), name='login'),
    path('logout', LogoutView.as_view (), name='logout'),
      path('register/', views.RegisterUser.as_view(),
        name='user-register',
    ),
]