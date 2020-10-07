from django.urls import path
from apps.asignacion_eq_maq.views import *

app_name = 'asignacion_ep_maq'

urlpatterns = [
    path('lista/', asig_eq_maq_list.as_view(), name='lista'),
    path('crear/', asig_eq_maq_create.as_view(), name='crear'),
    path('editar/<int:pk>/', asig_eq_maq_update.as_view(), name='editar'),
    path('eliminar/<int:pk>/', asig_eq_maq_delete.as_view(), name='eliminar'),

]
