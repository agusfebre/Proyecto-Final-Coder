from django.urls import path
from appviajandoando.views import principal


urlpatterns = [
    path ('', principal, name='viajandoando principal'),

]