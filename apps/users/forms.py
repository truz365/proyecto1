from django import forms
from django.contrib.auth import authenticate 
from django.contrib.auth.forms import UserCreationForm
from .models import *

from .models import User

class LoginForm(forms.Form):

    email = forms.CharField(
        label='Email',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Email'
            }
        )
    )

    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'****'
            }
        )
    )
    def clean(self):
        self.cleanned_data = super(LoginForm, self).clean()
        email = self.cleanned_data.get('email')
        password = self.cleanned_data.get('password')

        if not authenticate(email=email, password=password):
            raise forms.ValidationError('Datos de usuario incorrectos')
        return self.cleanned_data
    
class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Password", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['email', 'username', 'surname', 'password']

    def clean_password2 (self):
        if self.cleaned_data.get('password') !=  self.cleaned_data['password2']:
            self.add_error('password2', 'Las password no coinciden.')



