from django.urls import path
from apps.labor.views import *

app_name = 'labor'

urlpatterns = [
    path('lista/', labor_list.as_view(), name='lista'),
    path('crear/', labor_create.as_view(), name='crear'),
    path('editar/<int:pk>/', labor_update.as_view(), name='editar'),
    path('eliminar/<int:pk>/', labor_delete.as_view(), name='eliminar'),

]
