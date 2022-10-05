from django.db import models
from django.conf import settings
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify

# Create your models here.


CATEGORIAS = (
    ('Europa', 'europa'),
    ('Asia', 'asia'),
    ('Sudamerica', 'sudamerica'),
    ('Centro América', 'centro america'),
    ('Norte América', 'norte america'),
    ('Oceania', 'oceania'),
    ('Africa', 'africa')
) 

class Experiencia(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=1000)
    categoria = models.CharField(max_length=100, choices = CATEGORIAS)
    pais = models.CharField(max_length=1000)
    cuerpo = RichTextField(blank=True, null=True)
    foto = models.ImageField(upload_to='experiencias', null=True, blank=True)
    fecha = models.DateTimeField(default=datetime.now, blank=True)
    

    def __str__(self):
        return f'{self.titulo} by {self.autor}'




class Avatar(models.Model):
    #vinvulo con el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #Subcaperta avatares de media :) 
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
