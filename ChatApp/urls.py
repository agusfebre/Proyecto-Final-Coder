from django.urls import path
from .views import *
#import para cerrar sesión
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path ('', home, name="home"),
    path ('selectuser/', selectUser, name="selectUser"),
    path ('salaChat/', salaChat, name="salaChat"),
    #path ('salaChat/?receptor=recep/', salaChat, name="salaChat"),
   

]