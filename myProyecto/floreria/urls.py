from django.contrib import admin
from django.urls import path, include
from .views import inicio,galeria,ingresar,carrito,quienes, registro_usuario,FlorViewset, guardar_token
from rest_framework import routers
router = routers.DefaultRouter()
router.register('Flor',FlorViewset)
urlpatterns = [
    path('',inicio,name='INICIO'),
    path('galeria/',galeria,name='GALERIA'),
    path('ingresar',ingresar,name='INGRESAR'),
    path('carrito',carrito,name='CARRITO'),
    path('quienes/',quienes,name='QUIENES'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('registro/', registro_usuario,name='registro_usuario'),
    path('api/',include(router.urls)),
    path('guardar_token/', guardar_token, name='guardar_token'),
]