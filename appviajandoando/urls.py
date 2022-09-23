from django.urls import path
from appviajandoando.views import principal
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path ('', principal, name='principal'),

]

urlpatterns += staticfiles_urlpatterns()