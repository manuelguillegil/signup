from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrarUsuarioForm(forms.Form):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    password1 = forms.CharField(max_length=254, required=True)
    password2 = forms.CharField(max_length=254, required=True)

    class Meta:
        fields = ('email', 'password1', 'password2')

class IngresarUsuarioForm(forms.Form):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    password1 = forms.CharField(max_length=254, required=True, widget=forms.PasswordInput())
    class Meta:
        fields = ('email', 'password1')