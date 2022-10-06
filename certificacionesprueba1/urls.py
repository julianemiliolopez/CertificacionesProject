from django.urls import path
from . import views
from django.urls import re_path

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    path('', views.index, name='index'),
    path('categoria/mostrar',views.mostrar,name='mostrar'),
    path('categoria/bootstrap',views.bootstrap,name='bootstrap'),
    ##path('certificacionespedidos/mostrar',views.mostrarCertificacionesPedidos,name='mostrar'),
]