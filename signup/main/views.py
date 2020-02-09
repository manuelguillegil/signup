from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from main.forms import RegistrarUsuarioForm, IngresarUsuarioForm
from main.models import User_Information
import re

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
            user = User_Information(email = email, password = password1)
            user.save()
        else:
            mensaje = 'el form no es valido'
        
    mensaje = ''
    return render(request, 'thanks.html', {'mensaje': mensaje})

def registrarUsuario(email, password1, password2):
    if not User_Information.objects.filter(email=email).exists():
        correo,mensaje = verificarEmail(email)
        if (correo):
            if password1 == password2:
                if verificarPassword(password1):
                    return True
                else:
                    print("Clave Invalida")
                    return False
            else:
                print("Las claves no coinciden")
                return False
        else:
            print(mensaje)
            return False
    else:
        print('Correo ya registrado')
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

def verificarEmail(email):
    if re.match('\S*@\S*',email):
        if re.match('\S+@\S+',email):
            if re.match('\w+[.|\w]\w+@\w+[.]\w+[.|\w+]\w+', email):
                return True,''
            else:
                return False, 'Caracteres invalidos'
        else:
            return False,'Faltan campos antes o despues de @'
    else:
        return False,'Problema con @'
    
def verificarPassword(password):
    letras = 0
    mayus = 0
    minus = 0
    numeros = 0
    for i in range(len(password)):
        if ((password[i] >= 'a' and password[i] <= 'z')):
            letras += 1
            minus += 1
        elif (password[i] >= 'A' and password[i] <= 'Z'):
            letras += 1
            mayus += 1
        elif (password[i] >= '0' and password[i] <= '9'):
            numeros += 1
        else:
            print("Caracter '"+password[i]+"' invalido.")
            return False
    if (len(password) >= 8):
        if(len(password) <= 16):
            if letras >= 3:
                if minus >= 1: 
                    if mayus >= 1:
                        if numeros >= 1:
                            return True
                        else:
                            print('La contrasena debe contener al menos 1 numero')
                            return False
                    else:
                        print('La contrasena debe contener al menos 1 mayuscula')
                        return False
                else:
                    print('La contrasena debe contener al menos 1 minuscula')
                    return False
            else:
                print('La contrasena debe contener al menos 3 letras')
                return False
        else:
            print('La contrasena debe contener maximo 16 caracteres')
            return False
    else:
        print('La contrasena debe tener al menos 8 caracteres')
        return False