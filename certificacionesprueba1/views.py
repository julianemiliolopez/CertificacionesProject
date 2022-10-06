from django.shortcuts import render
from django.http import HttpResponse
from .models import Categorias
from .models import CertificacionesPedidos

# Create your views here.
def index(request):
    return HttpResponse("INDEX DE CERTIFICACIONES ")

def mostrar(request):
    ##a_record = Categorias()
    ##a_record.save()
    st=Categorias.objects.all()  # Collect all records from table 
    return render(request,'categorias/mostrar.html',{'st':st})
def bootstrap(request):
    ##a_record = Categorias()
    ##a_record.save()
    ##st=Categorias.objects.all()  # Collect all records from table 
    return render(request,'categorias/bootstrap5.html')

##def mostrarCertificacionesPedidos(request):
##	st=CertificacionesPedidos.objects.all()  # Collect all records from table 
##	return render(request,'mostrarcertificacionespedidos.html',{'st':st})