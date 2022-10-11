from django.contrib import admin
from .models import Categorias, Agrupamientos,  Certificaciones, Empresas, Personas, CertificacionesPedidos
# Register your models here.

admin.site.register(Categorias)
admin.site.register(Agrupamientos)
admin.site.register(Certificaciones)
admin.site.register(Personas)
admin.site.register(Empresas)
admin.site.register(CertificacionesPedidos)
