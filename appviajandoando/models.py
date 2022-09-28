from django.db import models

# Create your models here.

class entrada(models.Model):
    nombre = models.CharField(max_length=50)
    destino = models.CharField(max_length=20)
    comentario = models.TextField(max_length=500)
    fecha_posteo = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.nombre