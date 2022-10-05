from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    ##path('categoria/mostrar',views.mostrar,name='mostrar'),
    ##path('certificacionespedidos/mostrar',views.mostrarCertificacionesPedidos,name='mostrar'),
]