from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Experiencia


CATEGORIAS = (
    ('Europa', 'europa'),
    ('Asia', 'asia'),
    ('Sudamerica', 'sudamerica')
)

#Registro de Usuario
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

#Editar perfil de usuario
class UserEditForm(UserCreationForm):
    email=forms.EmailField(label='Modificar E-Mail')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)
    first_name=forms.CharField(label='Modificar Nombre')
    last_name=forms.CharField(label='Modificar Apellido')

    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2', 'first_name', 'last_name']
        help_texts = {k:"" for k in fields}

#Cargar Avatar a usuario
class AvatarForm(forms.Form):
    imagen= forms.ImageField(label="Imagen")
    
#Formulario para cargar experiencia de viaje
class ExperienciaForm(ModelForm):
    class Meta:
        
        model = Experiencia
        fields = [
            'titulo',  
            'subtitulo', 
            'categoria',
            'imagen',
            'cuerpo',
            
            ]
    
         
    
        
 