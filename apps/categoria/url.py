from django.urls import path
from apps.categoria.views import *
app_name= 'categoria'

urlpatterns = [
    path('lista/', categoria_list.as_view(), name='lista'),
    path('crear/', categoria_create.as_view(), name='crear'),
    path('editar/<int:pk>/', categoria_update.as_view(), name='editar'),
    path('eliminar/<int:pk>/', categoria_delete.as_view(), name='eliminar'),
]