from dataclasses import fields
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

class formPaquetes(forms.Form):
    nombre = forms.CharField(max_length=25)
    numero = forms.IntegerField()
    version = forms.CharField(max_length=5)
    documentacion = forms.CharField(max_length=255)
    licencia = forms.CharField(max_length=20)
    fecha = forms.DateField()
    precio = forms.CharField(max_length=20)
    imagen = forms.CharField(max_length=255)    

class UserRegisterForm(UserCreationForm):

    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label= 'Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'Re Pass', widget=forms.PasswordInput)

    first_name = forms.CharField()
    last_name = forms.CharField()
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'last_name', 'first_name']
        help_texts = {k:"" for k in fields}


class UserEditForm(UserCreationForm):

    email = forms.EmailField(label='Modificar Email')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Re-Pass', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}
