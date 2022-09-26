from django.shortcuts import render

from appviajandoando.forms import *
from appviajandoando.models import *

# Create your views here.

def principal(request):
    return render(request, 'index.html')
    
def europa(request):
    return render(request, 'appviajandoando/europa/europa.html')

def america(request):
    return render(request, 'appviajandoando/america/america.html')

def asia(request):
    return render(request, 'appviajandoando/asia/asia.html')