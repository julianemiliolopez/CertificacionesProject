from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Categorias, Maestro, Personas, SQLServerCategorias, SQLServerPersonas, SQLServerEmpresas,Empresas,SQLServerMaestro
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
	#q = request.GET.get('q')
	#error_msg = ''
	#if not q:
	#	error_msg = "Por favor ingrese un número de documento o nombre y apellido válidos"
	#	return render(request, 'solicitud/resultados.html', {'error_msg': error_msg})
	#lista_personas = Personas.objects.filter(Q(documento__icontains=q)|Q(apellido__icontains=q))
	return render(request, 'solicitud/crear.html', )

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



def convertirMaestro(request):
    ##a_record = Categorias()
    ##a_record.save()
    #st=Categorias.objects.all()  # Collect all records from table 
    st=SQLServerMaestro.objects.all().using('sqlserver')
    persona = Personas()
    for item in st.iterator():
        if Personas.objects.filter(documento=item.documento).exists():
            persona= Personas.objects.get(documento=item.documento)
        # resto de acciones cuando el pedido existe
        else:
        # acciones cuando el pedido no existe, redireccionas, envias un mensaje o cualquier opcion que consideres necesario para tratar este caso
            pass

        
        maestro = Maestro(documento=persona, legajo =item.legajo, fecha_proceso = item.fecha_proceso, empresa = item.empresa, estado = item.estado, fecha_ingreso = item.fecha_ingreso, fecha_egreso = item.fecha_egreso, dependencia = item.dependencia, cargo = item.cargo, cargo_reemplazo = item.cargo_reemplazo,cargo_retroactivo = item.cargo_retroactivo,cantidad_horas = item.cantidad_horas, antiguedad = item.antiguedad, antiguedad_decreto = item.antiguedad_decreto, seguro_obligatorio = item.seguro_obligatorio, seguro_familiar = item.seguro_familiar,seguro_colectivo = item.seguro_colectivo, maternidad_fecha_salida = item.maternidad_fecha_salida, maternidad_total_dias = item.maternidad_total_dias, licencia = item.licencia, sindicato_ate = item.sindicato_ate, sindicato_atsa = item.sindicato_atsa, sindicato_upcn = item.sindicato_upcn, dependencia_fisica = item.dependencia_fisica, aporte_jubilatorio = item.aporte_jubilatorio, sindicato_sat = item.sindicato_sat, obra_social = item.obra_social, obra_social_fam_cargo = item.obra_social_fam_cargo, vacaciones_dias = item.vacaciones_dias, caja_complementaria = item.caja_complementaria, situacion_revista = item.situacion_revista, fecha_liquidacion = item.fecha_liquidacion, tarea = item.tarea, legajo_historico = item.legajo_historico, motivo_baja = item.motivo_baja, derecho_ocupacion = item.derecho_ocupacion, art = item.art, idmaestro = item.idmaestro, origen= item.origen)     
        maestro.save()
     
    ##for item in st.iterator():g,
    ##     persona = Personas(documento=item.documento, apellido=item.apellido, apellidosolo=item.apellidosolo, nombre=item.nombre, domicilio=item.domicilio, telefono=item.telefono, email=item.email, localidad=item.localidad, fecha_de_nacimiento=item.fecha_de_nacimiento, id_cuenta=item.id_cuenta, caja_de_ahorro=item.caja_de_ahorro,sexo=item.sexo, imagen=item.imagen, cuil0=item.cuil0,cuil1=item.cuil1, aporte_solidario=item.aporte_solidario, psicofisicos_fecha = item.psicofisicos_fecha, psicofisicos_condicion = item.psicofisicos_condicion, psicofisicos_duracion = item.psicofisicos_duracion, cbuena_salud_fecha = item.cbuena_salud_fecha, cbuena_salud_condicion = item.cbuena_salud_condicion, creincidencia_fecha= item.creincidencia_fecha, creincidencia_condicion= item.creincidencia_condicion, cbu = item.cbu, const_patrimonial_desde = item.const_patrimonial_desde, const_patrimonial_hasta = item.const_patrimonial_hasta, const_patrimonial_condicion = item.const_patrimonial_condicion, origen = item.origen    )
    ##     persona.save()
    
    st=Maestro.objects.all()
    paginator = Paginator(st, 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    #return render(request, 'personas/mostrar.html', {'page_obj': page_obj})
    
    return render(request,'/home.html',{'st':st})