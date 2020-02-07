from django.shortcuts import render
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
    mensaje = 'que mas mi bro'
    return render(request, 'thanks.html', {'mensaje': mensaje})

def ingresarUsuario(request):
    mensaje = 'epa bro'
    return render(request, 'thanks.html', {'mensaje': mensaje})