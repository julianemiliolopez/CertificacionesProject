from django.shortcuts import render
from django.http import HttpResponse
from .models import Categorias
from .models import CertificacionesPedidos

# Create your views here.
def index(request):
    return HttpResponse("INDEX DE CERTIFICACIONES ")

def mostrar(request):
	st=Categorias.objects.all()  # Collect all records from table 
	return render(request,'mostrar.html',{'st':st})

##def mostrarCertificacionesPedidos(request):
##	st=CertificacionesPedidos.objects.all()  # Collect all records from table 
##	return render(request,'mostrarcertificacionespedidos.html',{'st':st})