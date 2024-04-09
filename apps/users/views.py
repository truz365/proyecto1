from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse 
from django.contrib.auth import authenticate, login, logout 
from django.http import HttpResponseRedirect
from django.views.generic import View 
from .forms import RegistrationForm
from .models import User



from django.views.generic.edit import (
    FormView,
    UpdateView,
    CreateView,
    DeleteView,
    
)
from .forms import LoginForm 


# Create your views here.

class loginUser(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('biblioteca:list-libros')

    def form_valid(self, form):
        user = authenticate(
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)
        return super(loginUser, self).form_valid(form)
    
class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'users:login'
            )
        )





class RegisterUser(FormView):
    template_name = 'registro.html'
    form_class = RegistrationForm
    success_url = '/login/'

    def form_valid(self, form):
        users = User.objects.create_user(
            form.cleaned_data['email'],
            form.cleaned_data['password'],
            username =form.cleaned_data['username'],
            surname = form.cleaned_data['surname'],
            usertype = 'VIEW',
            is_active = True,
        )
        return super().form_valid(form)