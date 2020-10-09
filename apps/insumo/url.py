from django.urls import path
from apps.insumo.views import *
app_name= 'insumo'

urlpatterns = [
    path('lista/', insumo_list.as_view(), name='lista'),
    path('crear/', insumo_create.as_view(), name='crear'),
    path('editar/<int:pk>/', insumo_update.as_view(), name='editar'),
    path('eliminar/<int:pk>/', insumo_delete.as_view(), name='eliminar'),
]