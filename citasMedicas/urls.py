"""citasMedicas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from apps.paciente.views import Home,Registro,BienvenidaView,añadir,registroCitas,listarCitas,eliminar,login,terminar
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home,name ='home'),
    path('home',Home,name ='home1'),
    path('registro/',Registro,name ='registro'),	
    path('inicio/',BienvenidaView,name ='inicio'),
    path('añadir/',añadir,name ='añadir'),
    path('registroCitas/',registroCitas,name ='registroCitas'),
    path('listarCitas/',listarCitas,name ='listarCitas'),
    path('eliminar/<int:id>',eliminar,name ='eliminar'),
    path('terminar',terminar,name ='terminar'),
    path('login/',login,name ='login'),
    path('paciente/', include('apps.paciente.urls')),
    #path('api/', include(('apps.api.urls','api'))),
    #url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, }),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 


