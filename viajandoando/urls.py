from django.contrib import admin
from django.urls import path, include

#Para las imagenes
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appviajandoando.urls')),
    path('', include('ChatApp.urls')),
 
]

#Para las imagenes
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
