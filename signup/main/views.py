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
    mensaje = 'El submit del form no es válido'
    form = RegistrarUsuarioForm(request.POST)
    if form.is_valid():
        email = form.cleaned_data['email']
        password1 = form.cleaned_data['password1']
        password2 = form.cleaned_data['password2']
        if (registrarUsuario(email, password1, password2)):
            mensaje = 'el form es validoooo'
            if not User_Information.objects.filter(email=email).exists():
                user = User_Information(email = email, password = password1)
                user.save()
        else:
            mensaje = 'el form no es valido'
        
    mensaje = ''
    return render(request, 'thanks.html', {'mensaje': mensaje})

def registrarUsuario(email, password1, password2):
    if not User_Information.objects.filter(email=email).exists():
        if ((email == '' or password1 == '' or password2 == '') or (password1 != password2)):
            return False
        return True
    else:
        return False

def loginPost(request):
    mensaje = 'El submit del form no es válido'
    form = IngresarUsuarioForm(request.POST)
    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password1']
        if (ingresarUsuario(email, password)):
            user = User_Information.objects.get(email=email)
            mensaje = 'Usuario aceptado'
            if (user.password != password):
                mensaje = 'Clave inválida'
        else:
            mensaje = 'Usuario inválido'
        

    return render(request, 'thanks.html', {'mensaje': mensaje})

def ingresarUsuario(email, password1):
    if (email == '' or password1 == ''):
            return False
    if (User_Information.objects.filter(email=email).exists()):
        user = User_Information.objects.get(email=email)
        if (user.password != password1):
            return False
        return True
    else:
        return False