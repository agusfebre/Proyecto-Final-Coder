from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
CATEGORIAS = (
    ('Europa', 'Europa'),
    ('Asia', 'Asia'),
    ('Sudamerica', 'Sudamerica')
)

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares',null=True, blank = True)

    
class Experiencia(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, default = User.username)
    titulo = models.CharField(max_length=100)
   # subtitulo = models.CharField(max_length=1000)
    categoria = models.CharField(max_length=100, choices = CATEGORIAS)
    cuerpo = RichTextField(blank=True, null=True)
    imagen = models.ImageField(blank=True)

    def __str__(self):
        return self.titulo
