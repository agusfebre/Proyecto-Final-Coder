from django.shortcuts import render

from appviajandoando.forms import *
from appviajandoando.models import *

# Create your views here.

def principal(request):
    return render(request, 'index.html')