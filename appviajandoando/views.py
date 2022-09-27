from http.client import HTTPResponse
from django.shortcuts import render

from appviajandoando.forms import *
from appviajandoando.models import *

# import para registrar un Usuario
from .forms import UserRegisterForm
from .models import *
#imports para login
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from datetime import datetime

# Create your views here.

def principal(request):
    return render(request, 'index.html')

def login_user(request):
    if request.method=="POST":
        form = AuthenticationForm(request, data=request.POST )
        if form.is_valid():
            usu=request.POST["username"]
            clave=request.POST["password"]

            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, 'login_user.html', {'mensaje':f"Bienvenido {usuario}"})
            else:
                return render(request, 'login_user.html', {"form":form, 'mensaje':'Usuario o contraseña incorrectos'})
        else:
            return render(request, 'login_user.html', {"form":form, 'mensaje':'Usuario o contraseña incorrectos'})
    else:
        form=AuthenticationForm()
        return render(request, 'login_user.html', {'form':form})


def registrate(request):
    if request.method=="POST":
        form= UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            #podriamos fijarnos que no exista un user en la bd con ese nombre

            form.save()
            return render(request, 'login_user.html', {'mensaje':f"Usuario {username} creado!"})
    else:
        form=UserRegisterForm()
    return render(request, 'registrate.html', {'form':form})


def europa(request):
    return render(request , 'europa.html')

def asia(request):
    return render(request , 'asia.html')