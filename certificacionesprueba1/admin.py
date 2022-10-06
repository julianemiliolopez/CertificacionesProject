from django.contrib import admin
from .models import Categorias, Agrupamientos,  Certificaciones, Personas
# Register your models here.

admin.site.register(Categorias)
admin.site.register(Agrupamientos)
admin.site.register(Certificaciones)
admin.site.register(Personas)