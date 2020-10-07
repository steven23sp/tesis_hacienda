from django.urls import path
from apps.equipo_maquinaria.views import *
app_name= 'equipo_maquinaria'

urlpatterns = [
    path('lista/', equi_maq_list.as_view(), name='lista_equipo_maquinaria'),
    path('crear/', equi_maq_create.as_view(), name='crear_equipo_maquinaria'),
    path('editar/<int:pk>/', equi_maq_update.as_view(), name='editar_equipo_maquinaria'),
    path('eliminar/<int:pk>/', equi_maq_delete.as_view(), name='eliminar_equipo_maquinaria'),
]