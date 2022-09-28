from django.urls import path
from appviajandoando.views import europa, principal, login_user, registrate, asia, america

#import para Statics Files
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

#import para cerrar sesión
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path ('', principal, name='principal'),
    path ('login_user/', login_user, name="login_user"),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path ('registrate/', registrate, name="registrate"),
    path('europa/', europa, name='europa'),
    path('asia/', asia, name='asia'),
    path('america/', america, name='america'),

]

urlpatterns += staticfiles_urlpatterns()