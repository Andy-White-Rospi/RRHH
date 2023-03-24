from django.urls import path
from .views import bol_per, guardar_per,borrar_per

urlpatterns = [
    path('',bol_per),
    path('guardar_per/',guardar_per,name='guardar_per'),
    path('borrar_per/<int:task_id>/',borrar_per,name='borrar_per')
]