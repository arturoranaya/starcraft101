from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='index'),
    path('<slug:slug>/', detalleEntrada, name='detalle_entrada'),
    # path('generales/', generales, name='generales'),
    # path('programacion/', programacion, name='programacion'),
    # path('videojuegos/', videojuegos, name='videojuegos'),
    # path('tecnologia/', tecnologia, name='tecnologia'),
    # path('tutoriales/', tutoriales, name='tutoriales'),
]
