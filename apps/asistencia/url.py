from django.urls import path

from apps.asistencia.views import *
app_name= 'asistencia'

urlpatterns = [
    path('lista/', asientencia_list.as_view(), name='lista'),
    path('crear/', asistencia_create.as_view(), name='crear'),
]