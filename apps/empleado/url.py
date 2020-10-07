from django.urls import path
from apps.empleado.views import *
app_name= 'empleado'

urlpatterns = [
    path('lista/', emple_list.as_view(), name='lista_empleado'),
    path('crear/', empleadao_create.as_view(), name='crear_empleado'),
    path('editar/<int:pk>/', empleadao_update.as_view(), name='editar_empleado'),
    path('eliminar/<int:pk>/', empleadao_delete.as_view(), name='eliminar_empleado'),
]