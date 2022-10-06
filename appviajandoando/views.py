from http.client import HTTPResponse
from django.shortcuts import render, redirect

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
#Requiere Logearse
from django.contrib.auth.decorators import login_required
#Para envio de Email 
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string
from django.views.generic import TemplateView


# Create your views here.

def principal(request):
    experiencias=Experiencia.objects.all()
    avatares=Avatar.objects.all()
    if not experiencias:
        return render(request, 'principal.html', {"imagen":obtenerAvatar(request), "avatares":avatares, 'mensaje':'No se cargaron experiencias aún.'}) 
    else:
        experiencias_new = []
        for exp in experiencias:
            exp.cuerpo=exp.cuerpo.split('</p>')[0]
            if len(exp.cuerpo) > 250:
                exp.cuerpo=exp.cuerpo[0:250]
                exp.cuerpo=exp.cuerpo+'...'
            experiencias_new.append(exp)
        experiencias_new=reversed(experiencias_new)

        return render(request, 'index.html',  {"imagen":obtenerAvatar(request), "experiencias":experiencias_new, "avatares":avatares }) 
        

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
                return render(request, 'index.html', {'mensaje':f"Bienvenido {usuario}", "imagen":obtenerAvatar(request)})
            else:
                return render(request, 'login_user.html', {"form":form, 'mensaje':'Usuario o contraseña incorrectos'})
        else:
            return render(request, 'login_user.html', {"form":form, 'mensaje':'Usuario o contraseña incorrectos'})
    else:
        form=AuthenticationForm()
        return render(request, 'login_user.html', {'form':form, "imagen":obtenerAvatar(request)})

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
    
@login_required
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
            return render(request, 'index.html', {'mensaje':f"Perfil {usuario} editado correctamente.", "imagen":obtenerAvatar(request)})
    else:
        form= UserEditForm(instance=usuario)
    return render(request, 'editarPerfil.html', {'form':form, 'usuario':usuario, "imagen":obtenerAvatar(request)})


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
    if str(request.user) == 'AnonymousUser':
        return ""        
    lista=Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        imagen=lista[0].imagen.url
    else:
        imagen=""
    return imagen  

def europa(request):
    experiencias=Experiencia.objects.filter(categoria='Europa')
    avatares=Avatar.objects.all()
    if not experiencias:
        return render(request, 'europa.html', {"imagen":obtenerAvatar(request), "avatares":avatares, 'mensaje':'No se cargaron experiencias aún.'}) 
    else:
        experiencias_new = []
        for exp in experiencias:
            exp.cuerpo=exp.cuerpo.split('</p>')[0]
            if len(exp.cuerpo) > 250:
                exp.cuerpo=exp.cuerpo[0:250]
                exp.cuerpo=exp.cuerpo+'...'
            experiencias_new.append(exp)
        experiencias_new=reversed(experiencias_new)
        return render(request, 'europa.html',  {"imagen":obtenerAvatar(request), "experiencias":experiencias_new, "avatares":avatares })

def asia(request):
    experiencias=Experiencia.objects.filter(categoria='Asia')
    avatares=Avatar.objects.all()
    if not experiencias:
        return render(request, 'asia.html', {"imagen":obtenerAvatar(request), "avatares":avatares, 'mensaje':'No se cargaron experiencias aún.'}) 
    else:
        experiencias_new = []
        for exp in experiencias:
            exp.cuerpo=exp.cuerpo.split('</p>')[0]
            if len(exp.cuerpo) > 250:
                exp.cuerpo=exp.cuerpo[0:250]
                exp.cuerpo=exp.cuerpo+'...'
            experiencias_new.append(exp)
        experiencias_new=reversed(experiencias_new)
        return render(request, 'asia.html',  {"imagen":obtenerAvatar(request), "experiencias":experiencias_new, "avatares":avatares })

def america(request):
    experiencias=Experiencia.objects.filter(categoria='Sudamerica')
    avatares=Avatar.objects.all()
    if not experiencias:
        return render(request, 'america.html', {"imagen":obtenerAvatar(request), "avatares":avatares, 'mensaje':'No se cargaron experiencias aún.'}) 
    else:
        experiencias_new = []
        for exp in experiencias:
            exp.cuerpo=exp.cuerpo.split('</p>')[0]
            if len(exp.cuerpo) > 250:
                exp.cuerpo=exp.cuerpo[0:250]
                exp.cuerpo=exp.cuerpo+'...'
            experiencias_new.append(exp)
        experiencias_new=reversed(experiencias_new)
        return render(request, 'america.html',  {"imagen":obtenerAvatar(request), "experiencias":experiencias_new, "avatares":avatares })

def ultimasExperiencias(request):
    experiencias=Experiencia.objects.all()
    avatares=Avatar.objects.all()
    if not experiencias:
        return render(request, 'ultimasExperiencias.html', {"imagen":obtenerAvatar(request), "avatares":avatares, 'mensaje':'No se cargaron experiencias aún.'}) 
    else:
        experiencias_new = []
        for exp in experiencias:
            exp.cuerpo=exp.cuerpo.split('</p>')[0]
            if len(exp.cuerpo) > 250:
                exp.cuerpo=exp.cuerpo[0:250]
                exp.cuerpo=exp.cuerpo+'...'
            experiencias_new.append(exp)
        experiencias_new=reversed(experiencias_new)
        return render(request, 'ultimasExperiencias.html',  {"imagen":obtenerAvatar(request), "experiencias":experiencias_new, "avatares":avatares })  

def acercade(request):
    return render(request, 'acercade.html', {"imagen":obtenerAvatar(request)})

def cargarexperiencia(request):
    if request.method == 'POST':
        form = ExperienciaForm(request.POST, request.FILES)
        if form.is_valid():
            info= form.cleaned_data
            autor= info["autor"]
            titulo= info["titulo"]
            subtitulo= info["subtitulo"]
            pais= info["pais"]
            categoria= info["categoria"]
            foto= info["foto"]
            cuerpo= info["cuerpo"]
            carga_exp= Experiencia(autor=autor, titulo=titulo, subtitulo=subtitulo, pais=pais, categoria=categoria, foto=foto, cuerpo=cuerpo)
            carga_exp.save()
            
            return render(request, 'index.html', {'usuario':request.user, 'mensaje':'Cargaste una experiencia nueva al Blog, Muchas gracias por tu colaboración.', "imagen":obtenerAvatar(request)})
    else:
        form = ExperienciaForm()
    return render(request, 'nueva_experiencia.html', {'form':form, "imagen":obtenerAvatar(request)})

def editarExperiencia(request,id):
    #Traer Experiencia a editar
    experiencia = Experiencia.objects.get(id = id)

    if request.method == 'POST':
        #Viene lleno el formulario con los datos de la experiencia a editar
        form = ExperienciaForm(request.POST, request.FILES)

        if form.is_valid():
            #Cambio los datos
            informacion = form.cleaned_data
            
            print(str(informacion))

            experiencia.autor=informacion['autor']
            experiencia.titulo=informacion['titulo']
            experiencia.subtitulo=informacion['subtitulo']
            experiencia.pais=informacion['pais']
            experiencia.categoria=informacion['categoria']
            experiencia.foto=informacion['foto']
            experiencia.cuerpo=informacion['cuerpo']
		    #Guardo el formulario modificado
            experiencia.save()
            return render(request, "index.html")

    else:
        form= ExperienciaForm(
             initial={
                'autor': experiencia.autor, 
                'titulo':experiencia.titulo , 
                'subtitulo':experiencia.subtitulo, 
                'pais':experiencia.pais ,
                'categoria':experiencia.categoria , 
                'foto':experiencia.foto,
                'cuerpo':experiencia.cuerpo,
            }
        )
    return render(request, "editarExperiencia.html", {"formu": form, "titulo":experiencia.titulo, "id":experiencia.id})
        
def eliminarExperiencia(request, id):
    experiencia = Experiencia.objects.get(id=id)
    experiencia.delete()
    experiencia = Experiencia.objects.all()
    contexto ={"experiencia":experiencia}
    return render(request,"index.html",contexto)

def leerExperiencia(request, id):
    experiencia=Experiencia.objects.get(id=id)
    avatares=Avatar.objects.all()
    print(experiencia)
    return render(request, "leerExperiencia.html", {"experiencia":experiencia, "id":experiencia.id, "avatares":avatares})

#Contacto
def contacto(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']
            html = render_to_string('envioFormularioContacto.html',{
                'name': name,
                'email':email,
                'content':content

            })

            send_mail(f'{name} consulta desde el blog "ViajandoAndo" ', 'This is the message','noreply@viajandoando.com', ['jonnyvm@hotmail.com'],html_message=html)
            return redirect('contacto')
    else:
        form = ContactForm()
    
    return render(request, 'contacto.html', {'form':form})


