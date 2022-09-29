from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify

# Create your models here.

class entrada(models.Model):
    nombre = models.CharField(max_length=50)
    destino = models.CharField(max_length=20)
    comentario = models.TextField(max_length=500)
    fecha_posteo = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.nombre

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
    autor = models.ForeignKey(User, on_delete=models.CASCADE, default = User.username)
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=1000)
    categoria = models.CharField(max_length=100, choices = CATEGORIAS)
    cuerpo = RichTextField(blank=True, null=True)
    imagen = models.ImageField(blank=True)

    def __str__(self):
        return self.titulo + self.subtitulo

def get_image_filename(instance, filename):
    title =  'titulo'
    slug = slugify(title)
    return "imagenesAvatares/%s-%s" % (slug, filename)  


class Avatar(models.Model):
    #vinvulo con el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #Subcaperta avatares de media :) 
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

    def __str__(self):
        return f"Imagen de: {self.user.username}"

