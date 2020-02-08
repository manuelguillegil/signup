from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from main.forms import RegistrarUsuarioForm, IngresarUsuarioForm
from main.models import User_Information

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

def signupPost(request):
    form = RegistrarUsuarioForm(request.POST)
    if form.is_valid():
        email = form.cleaned_data['email']
        password1 = form.cleaned_data['password1']
        password2 = form.cleaned_data['password2']
        if (registrarUsuario(email, password)):
            mensaje = 'el form es validoooo'
            if not User_Information.objects.filter(email=email).exists():
                user = User_information(email = email, password = password1)
                user.save()
        else:
            mensaje = 'el form no es valido'
        
    mensaje = ''
    return render(request, 'thanks.html', {'mensaje': mensaje})

def registrarUsuario(email, password1, password2):
    return True

def loginPost(request):
    mensaje = ''
    form = IngresarUsuarioForm(request.POST)
    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password1']
        if (ingresarUsuario(email, password)):
            mensaje = 'el form es validoooo'
        else:
            mensaje = 'el form no es valido'
        

    return render(request, 'thanks.html', {'mensaje': mensaje})

def ingresarUsuario(email, password1):
    if (email == '' or password1 == ''):
        return False
    return True