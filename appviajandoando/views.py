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
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, 'index.html', {"url":avatares[0].imagen.url})

def urlImagen():

      return "/media/avatares/avatar_01.png"

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

def editarPerfil(request):
    usuario=request.user
    if request.method=="POST":
        form= UserEditForm(request.POST)
        if form.is_valid():
            usuario.first_name=form.cleaned_data["first_name"]
            usuario.last_name=form.cleaned_data["last_name"]
            usuario.email=form.cleaned_data["email"]
            usuario.password1=form.cleaned_data["password1"]
            usuario.password2=form.cleaned_data["password2"]
            usuario.save()
            return render(request, 'index.html', {'mensaje':f"Perfil {usuario} editado correctamente."})
    else:
        form= UserEditForm(instance=usuario)
    return render(request, 'editarPerfil.html', {'form':form, 'usuario':usuario})


def agregarAvatar(request):
    if request.method == 'POST':
        formulario=AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():
            avatarViejo=Avatar.objects.filter(user=request.user)
            if(len(avatarViejo)>0):
                avatarViejo.delete()
            avatar=Avatar(user=request.user, imagen=formulario.cleaned_data['imagen'])
            avatar.save()
            return render(request, 'index.html', {'usuario':request.user, 'mensaje':'AVATAR AGREGADO EXITOSAMENTE', "imagen":obtenerAvatar(request)})
    else:
        formulario=AvatarForm()
    return render(request, 'agregarAvatar.html', {'form':formulario, 'usuario':request.user, "imagen":obtenerAvatar(request)})

#####funcion que trae la url del avatar###
def obtenerAvatar(request):
    lista=Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        imagen=lista[0].imagen.url
    else:
        imagen=""
    return imagen  

def europa(request):
    return render(request , 'europa.html')

def asia(request):
    return render(request , 'asia.html')


def america(request):
    return render(request, 'america.html')

def cargarexperiencia(request):
    if request.method == 'POST':
        form = ExperienciaForm(request.POST)
        if form.is_valid():
            post_item = form.save(commit=False)
            post_item.save()
            return redirect('/')
    else:
        form = ExperienciaForm()
    return render(request, 'nueva_experiencia.html', {'form':form})

