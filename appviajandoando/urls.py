from django.urls import path
from appviajandoando.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path ('', principal, name='principal'),
    path ('europa/', europa, name='europa'),
    path ('america/', america, name='america'),
    path ('asia/', asia, name='asia'),

]

urlpatterns += staticfiles_urlpatterns()