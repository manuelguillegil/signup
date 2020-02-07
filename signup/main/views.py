from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from main.forms import RegistrarUsuarioForm, IngresarUsuarioForm

# Create your views here.
def index(request):
    return render(request,'home.html',{'variable':''})

def signup(request):
    form = RegistrarUsuarioForm()
    return render(request,'signup.html',{'form':form})

def login(request):
    form = IngresarUsuarioForm()
    return render(request,'login.html',{'form':form})

def thanks(request):
    return render(request, 'thanks.html', {'user': request})

def registrarUsuario(request):
    form = RegistrarUsuarioForm(request.POST)
    if form.is_valid():
        email = form.cleaned_data['email']
        password1 = form.cleaned_data['password1']
        password2 = form.cleaned_data['password2']
        
    mensaje = ''
    return render(request, 'thanks.html', {'mensaje': mensaje})

def ingresarUsuario(request):
    form = IngresarUsuarioForm(request.POST)
    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password1']

    mensaje = ''
    return render(request, 'thanks.html', {'mensaje': mensaje})
