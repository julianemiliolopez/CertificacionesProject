from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Categorias, Personas, SQLServerCategorias, SQLServerPersonas, SQLServerEmpresas,Empresas
from .models import CertificacionesPedidos
from django.shortcuts import render
from django.core.paginator import Paginator

from django.db.models import Q


# Create your views here.
def index(request):
    return render(request, "home.html",{})

def mostrarCategoriasSQLServer(request):
    ##a_record = Categorias()
    ##a_record.save()
    ##st=Categorias.objects.all()  # Collect all records from table 
    st=SQLServerCategorias.objects.all().using('sqlserver')
    
    return render(request,'categorias/mostrar.html',{'st':st})

def mostrarPersonasSQLServer(request):
    ##a_record = Categorias()
    ##a_record.save()
    ##st=Categorias.objects.all()  # Collect all records from table 
    ##st=Personas.objects.all().using('sqlserver')

     
    ##for item in st.iterator():
    ##     persona = Personas(documento=item.documento, apellido=item.apellido, apellidosolo=item.apellidosolo, nombre=item.nombre, domicilio=item.domicilio, telefono=item.telefono, email=item.email, localidad=item.localidad, fecha_de_nacimiento=item.fecha_de_nacimiento, id_cuenta=item.id_cuenta, caja_de_ahorro=item.caja_de_ahorro,sexo=item.sexo, imagen=item.imagen, cuil0=item.cuil0,cuil1=item.cuil1, aporte_solidario=item.aporte_solidario, psicofisicos_fecha = item.psicofisicos_fecha, psicofisicos_condicion = item.psicofisicos_condicion, psicofisicos_duracion = item.psicofisicos_duracion, cbuena_salud_fecha = item.cbuena_salud_fecha, cbuena_salud_condicion = item.cbuena_salud_condicion, creincidencia_fecha= item.creincidencia_fecha, creincidencia_condicion= item.creincidencia_condicion, cbu = item.cbu, const_patrimonial_desde = item.const_patrimonial_desde, const_patrimonial_hasta = item.const_patrimonial_hasta, const_patrimonial_condicion = item.const_patrimonial_condicion, origen = item.origen    )
    ##     persona.save()
    
    st=Personas.objects.all()
    paginator = Paginator(st, 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'personas/mostrar.html', {'page_obj': page_obj})
    
    ##return render(request,'personas/mostrar.html',{'st':st})



def buscarPersona(request,documento):
    try:
        persona=Personas.objects.using('sqlserver').get(documento=documento)
    except Personas.DoesNotExist:
        raise Http404("La persona no existe")

    #book_id=get_object_or_404(Book, pk=pk)

    return render(
        request,
        'personas/detalle.html',
        context={'Persona':persona,}
    )



def busqueda(request):
    return render(request, "solicitud/busqueda.html",{})

def buscar(request):
	q = request.GET.get('q')
	error_msg = ''
	if not q:
		error_msg = "Por favor ingrese un número de documento o nombre y apellido válidos"
		return render(request, 'solicitud/resultados.html', {'error_msg': error_msg})
	lista_personas = Personas.objects.filter(Q(documento__icontains=q)|Q(apellido__icontains=q))
	return render(request, 'solicitud/resultados.html', {'error_msg': error_msg, 'lista_personas': lista_personas})

def crear(request):
	q = request.GET.get('q')
	error_msg = ''
	if not q:
		error_msg = "Por favor ingrese un número de documento o nombre y apellido válidos"
		return render(request, 'solicitud/resultados.html', {'error_msg': error_msg})
	lista_personas = Personas.objects.filter(Q(documento__icontains=q)|Q(apellido__icontains=q))
	return render(request, 'solicitud/resultados.html', {'error_msg': error_msg, 'lista_personas': lista_personas})

def modificar(request):
	q = request.GET.get('q')
	error_msg = ''
	if not q:
		error_msg = "Por favor ingrese un número de documento o nombre y apellido válidos"
		return render(request, 'solicitud/resultados.html', {'error_msg': error_msg})
	lista_personas = Personas.objects.filter(Q(documento__icontains=q)|Q(apellido__icontains=q))
	return render(request, 'solicitud/resultados.html', {'error_msg': error_msg, 'lista_personas': lista_personas})

def eliminar(request):
	q = request.GET.get('q')
	error_msg = ''
	if not q:
		error_msg = "Por favor ingrese un número de documento o nombre y apellido válidos"
		return render(request, 'solicitud/resultados.html', {'error_msg': error_msg})
	lista_personas = Personas.objects.filter(Q(documento__icontains=q)|Q(apellido__icontains=q))
	return render(request, 'solicitud/resultados.html', {'error_msg': error_msg, 'lista_personas': lista_personas})


def bootstrap(request):
    ##a_record = Categorias()
    ##a_record.save()
    ##st=Categorias.objects.all()  # Collect all records from table 
    return render(request,'categorias/bootstrap5.html')

##def mostrarCertificacionesPedidos(request):
##	st=CertificacionesPedidos.objects.all()  # Collect all records from table 
##	return render(request,'mostrarcertificacionespedidos.html',{'st':st})


def empresasSQLServer(request):
    ##a_record = Categorias()
    ##a_record.save()
    #st=Categorias.objects.all()  # Collect all records from table 
    st=Empresas.objects.all().using('sqlserver')

     
    for item in st.iterator():
         empresa = Empresas(documento=item.documento, apellido=item.apellido, apellidosolo=item.apellidosolo, nombre=item.nombre, domicilio=item.domicilio, telefono=item.telefono, email=item.email, localidad=item.localidad, fecha_de_nacimiento=item.fecha_de_nacimiento, id_cuenta=item.id_cuenta, caja_de_ahorro=item.caja_de_ahorro,sexo=item.sexo, imagen=item.imagen, cuil0=item.cuil0,cuil1=item.cuil1, aporte_solidario=item.aporte_solidario, psicofisicos_fecha = item.psicofisicos_fecha, psicofisicos_condicion = item.psicofisicos_condicion, psicofisicos_duracion = item.psicofisicos_duracion, cbuena_salud_fecha = item.cbuena_salud_fecha, cbuena_salud_condicion = item.cbuena_salud_condicion, creincidencia_fecha= item.creincidencia_fecha, creincidencia_condicion= item.creincidencia_condicion, cbu = item.cbu, const_patrimonial_desde = item.const_patrimonial_desde, const_patrimonial_hasta = item.const_patrimonial_hasta, const_patrimonial_condicion = item.const_patrimonial_condicion, origen = item.origen    )
         empresa.save()
    
    st=Empresas.objects.all()
    paginator = Paginator(st, 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'personas/mostrar.html', {'page_obj': page_obj})