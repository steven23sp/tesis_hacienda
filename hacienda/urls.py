"""hacienda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.conf.urls import include
from apps.empleado.url import *
from apps.categoria.url import *
from apps.proveedor.url import *
from apps.asistencia.url import *
from apps.equipo_maquinaria.url import *
from apps.asignacion_eq_maq.url import *
from apps.labor.url import *
urlpatterns = [
    path('admin/', admin.site.urls),
    #empresa
    path('empleado/', include('apps.empleado.url', namespace='empleado')),
    path('cliente/', include('apps.cliente.url', namespace='cliente')),
    path('categoria/', include('apps.categoria.url', namespace='categoria')),
    path('proveedor/', include('apps.proveedor.url', namespace='proveedor')),
    path('asistencia/', include('apps.asistencia.url', namespace='asistencia')),
    path('equi_maqui/', include('apps.equipo_maquinaria.url', namespace='equipo_maquinaria')),
    path('asignacion_equi_maqui/', include('apps.asignacion_eq_maq.url', namespace='asignacion_equipo_maquina')),
    path('labor/', include('apps.labor.url', namespace='labor'))
]
