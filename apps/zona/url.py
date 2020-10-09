from django.urls import path
from apps.zona.views import *

app_name = 'zona'

urlpatterns = [
    path('lista/', zona_list.as_view(), name='lista'),
    path('crear/', zona_create.as_view(), name='crear'),
    path('editar/<int:pk>/', zona_update.as_view(), name='editar'),
    path('eliminar/<int:pk>/', zona_delete.as_view(), name='eliminar'),

]
