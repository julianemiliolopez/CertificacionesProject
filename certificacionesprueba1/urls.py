from django.urls import path
from . import views
from django.urls import re_path

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    path('', views.index, name='index'),
    path('categoria/mostrar',views.mostrarCategoriasSQLServer,name='mostrar'),
    path('categoria/bootstrap',views.bootstrap,name='bootstrap'),
    ##path('personas/mostrar',views.mostrarPersonas,name='Mostrar Personas'),
    path('personas/detalle',views.mostrarPersonasSQLServer,name='Mostrar Personas'),
    path('solicitud/busqueda/', views.busqueda, name='busqueda'),
    
   path('solicitud/resultados/', views.buscar, name='resultados')
    
    ##path('certificacionespedidos/mostrar',views.mostrarCertificacionesPedidos,name='mostrar'),
]