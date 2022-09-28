from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from datetime import datetime

# Create your views here.

def home(request):
    return render (request, "home.html")


def salaChat(request):
    
    #Elementos del mensaje
    emisor = str(request.POST['emisor'])

    #Receptor del mensaje
    recep = str(request.POST['receptor'])

    #Mensaje escrito
    txt = str(request.POST['text'])

    if txt != None and txt != "None" and txt != "":
        newMessage = Message.objects.create(emisor=emisor, receptor=recep, text=txt)
        newMessage.save()
    
    variable_historial = []
    histo=Message.objects.all()
    for h in histo:
        #El siguiente if se podria quitar si bloqueo el boton de enviar mensaje hasta que tenga algo escrito en el box?
        if h.text != "None" and h.text != "None" and h.text != "" and ((h.emisor == emisor and h.receptor == recep) or (h.emisor == recep and h.receptor == emisor)):
            registro = {
                            "emisor":h.emisor,
                            "mensaje":str(h.text),
                            "fecha": h.date.strftime('%H:%M') if (h.date.strftime('%Y-%m-%d') == datetime.today().strftime('%Y-%m-%d')) else h.date.strftime('%Y-%m-%d %H:%M')
                        }
            variable_historial.append(registro)

    return render (request, "ChatApp/salaChat.html", {"recep":recep, "historial":variable_historial})

def selectUser(request):
    users= User.objects.all() #Todos los usuarios registrados
    return render (request, "ChatApp/selectuser.html", {"users":users})
