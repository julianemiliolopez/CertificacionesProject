# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Agrupamientos(models.Model):
    codigo = models.CharField(db_column='Codigo', max_length=2)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=30)  # Field name made lowercase.
    docente = models.CharField(db_column='Docente', max_length=1, blank=True, null=True)  # Field name made lowercase.
    codigo_ibm = models.CharField(db_column='Codigo IBM', max_length=1, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    idd = models.AutoField(db_column='Idd', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Agrupamientos'
    def __str__(self):
        return self.field_name
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])



class CertifCeroDias(models.Model):
    legajo = models.DecimalField(primary_key=True, db_column='Legajo', max_digits=18, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Certif Cero Dias'


class Certificaciones(models.Model):
    documento = models.DecimalField(db_column='Documento', max_digits=18, decimal_places=0)  # Field name made lowercase.
    legajo = models.DecimalField(db_column='Legajo', max_digits=18, decimal_places=0)  # Field name made lowercase.
    planilla = models.AutoField(db_column='Planilla', primary_key=True)  # Field name made lowercase.
    empresa = models.ForeignKey('Empresas', on_delete=models.CASCADE, db_column='Empresa', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fecha_pedido = models.DateTimeField(db_column='Fecha Pedido', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cargo = models.ForeignKey('Categorias', on_delete=models.CASCADE, db_column='Cargo', blank=True, null=True)  # Field name made lowercase.
    agrupamiento = models.ForeignKey(Agrupamientos, on_delete=models.CASCADE, db_column='Agrupamiento', blank=True, null=True)  # Field name made lowercase.
    causa = models.ForeignKey('CertificacionesCausas', on_delete=models.CASCADE, db_column='Causa', blank=True, null=True)  # Field name made lowercase.
    causa_cesacion = models.CharField(db_column='Causa Cesacion', max_length=600, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fecha_cesacion = models.DateTimeField(db_column='Fecha Cesacion', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fecha_ingreso = models.DateTimeField(db_column='Fecha Ingreso', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fecha_egreso = models.DateTimeField(db_column='Fecha Egreso', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fecha_haberes = models.DateTimeField(db_column='Fecha Haberes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    obs_rh_cert = models.CharField(db_column='Obs. RH Cert', max_length=1000, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    obs_dgh_cert = models.CharField(db_column='Obs. DGH Cert', max_length=600, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    obs_cesacion = models.CharField(db_column='Obs. Cesacion', max_length=600, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fecha_pase_rh = models.DateTimeField(db_column='Fecha Pase RH', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fecha_pase_dgh = models.DateTimeField(db_column='Fecha Pase DGH', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fecha_desde = models.DateTimeField(db_column='Fecha Desde', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fecha_hasta = models.DateTimeField(db_column='Fecha Hasta', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    control = models.CharField(db_column='Control', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tipo_certificado = models.CharField(db_column='Tipo Certificado', max_length=1, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fecha_nota = models.DateTimeField(db_column='Fecha Nota', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    obsdgh = models.CharField(db_column='ObsDGH', max_length=600, blank=True, null=True)  # Field name made lowercase.
    obsrh = models.CharField(db_column='ObsRH', max_length=800, blank=True, null=True)  # Field name made lowercase.
    fechaentrega = models.DateTimeField(db_column='FechaEntrega', blank=True, null=True)  # Field name made lowercase.
    obsfechaentrega = models.CharField(db_column='ObsFechaEntrega', max_length=200, blank=True, null=True)  # Field name made lowercase.
    opcentrega = models.IntegerField(db_column='OpcEntrega', blank=True, null=True)  # Field name made lowercase.
    oficinacertificante = models.CharField(db_column='OficinaCertificante', max_length=50, blank=True, null=True)  # Field name made lowercase.
    jefecertificante = models.CharField(db_column='JefeCertificante', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Certificaciones'
        unique_together = (('documento', 'legajo', 'planilla'),)


class CertificacionesAusenciasjustif(models.Model):
    documento = models.FloatField( primary_key=True, db_column='Documento')  # Field name made lowercase.
    legajo = models.FloatField(db_column='Legajo', blank=True, null=True)  # Field name made lowercase.
    empresa = models.CharField(db_column='Empresa', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cat_revista = models.FloatField(db_column='Cat revista', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cat_actual = models.FloatField(db_column='Cat actual', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    agrupamiento = models.CharField(db_column='Agrupamiento', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dependencia = models.FloatField(db_column='Dependencia', blank=True, null=True)  # Field name made lowercase.
    estado = models.FloatField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    fecdesde = models.DateTimeField(db_column='FecDesde', blank=True, null=True)  # Field name made lowercase.
    fechasta = models.DateTimeField(db_column='FecHasta', blank=True, null=True)  # Field name made lowercase.
    tdia = models.FloatField(db_column='TDia', blank=True, null=True)  # Field name made lowercase.
    tobl = models.FloatField(db_column='TObl', blank=True, null=True)  # Field name made lowercase.
    thor = models.FloatField(db_column='THor', blank=True, null=True)  # Field name made lowercase.
    j = models.CharField(db_column='J', max_length=255, blank=True, null=True)  # Field name made lowercase.
    art = models.FloatField(db_column='Art', blank=True, null=True)  # Field name made lowercase.
    desc_articulo = models.CharField(db_column='Desc  Articulo', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tiponov = models.CharField(db_column='TipoNov', max_length=255, blank=True, null=True)  # Field name made lowercase.
    comentario = models.CharField(db_column='Comentario', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Certificaciones AusenciasJustif'


class CertificacionesCausas(models.Model):
    idd = models.AutoField(db_column='Idd', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=45)  # Field name made lowercase.
    abreviatura = models.CharField(db_column='Abreviatura', max_length=8)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Certificaciones Causas'


class CertificacionesEstados(models.Model):
    estado = models.CharField(db_column='Estado', max_length=2, blank=True, null=True)  # Field name made lowercase.
    prioridad = models.DecimalField(db_column='Prioridad', max_digits=1, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    descripcion_larga = models.CharField(db_column='Descripcion Larga', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    idd = models.AutoField(db_column='Idd', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Certificaciones Estados'


class CertificacionesJubordinaria(models.Model):
    idd = models.AutoField(db_column='Idd', primary_key=True)
    anio = models.IntegerField(db_column='Anio')  # Field name made lowercase.
    edadmujer = models.IntegerField(db_column='EdadMujer')  # Field name made lowercase.
    edadhombre = models.IntegerField(db_column='EdadHombre')  # Field name made lowercase.
    aniosmujer = models.IntegerField(db_column='AniosMujer')  # Field name made lowercase.
    anioshombre = models.IntegerField(db_column='AniosHombre')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Certificaciones JubOrdinaria'


class CertificacionesObservaciones(models.Model):
    idd = models.AutoField(db_column='Idd', primary_key=True)  # Field name made lowercase.
    planilla = models.DecimalField(db_column='Planilla', max_digits=18, decimal_places=0)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=50)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=600)  # Field name made lowercase.
    dependencia = models.CharField(db_column='Dependencia', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Certificaciones Observaciones'
        unique_together = (('idd', 'planilla'),)


class CertificacionesPedidos(models.Model):
    idd = models.AutoField(db_column='IDD', primary_key=True)  # Field name made lowercase.
    empresa = models.ForeignKey('Empresas', on_delete=models.CASCADE, db_column='Empresa')  # Field name made lowercase.
    documento = models.DecimalField(db_column='Documento', max_digits=18, decimal_places=0)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=40, blank=True, null=True)  # Field name made lowercase.
    fecha_pedido = models.DateTimeField(db_column='Fecha Pedido')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    estado = models.ForeignKey(CertificacionesEstados, on_delete=models.CASCADE, db_column='Estado')  # Field name made lowercase.
    nronota = models.CharField(db_column='NroNota', max_length=10, blank=True, null=True)  # Field name made lowercase.
    prioridad = models.IntegerField(db_column='Prioridad')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=50, blank=True, null=True)  # Field name made lowercase.
    movim = models.CharField(db_column='Movim', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Certificaciones Pedidos'


class CertificacionesRemuneracion(models.Model):
    documento = models.DecimalField(db_column='Documento',  max_digits=18, decimal_places=0)  # Field name made lowercase.
    legajo = models.DecimalField(db_column='Legajo', max_digits=18, decimal_places=0)  # Field name made lowercase.
    planilla = models.DecimalField(db_column='Planilla', max_digits=18, decimal_places=0)  # Field name made lowercase.
    renglon = models.AutoField(db_column='Renglon', primary_key=True)  # Field name made lowercase.
    anio = models.DecimalField(db_column='Anio', max_digits=18, decimal_places=0)  # Field name made lowercase.
    con_aporte = models.DecimalField(db_column='Con Aporte', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    total = models.DecimalField(db_column='Total', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sac = models.DecimalField(db_column='SAC', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    reservado = models.DecimalField(db_column='Reservado', max_digits=18, decimal_places=2)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Certificaciones Remuneracion'
        unique_together = (('documento', 'legajo', 'planilla', 'renglon'),)


class CertificacionesServicios(models.Model):
    documento = models.DecimalField(db_column='Documento', max_digits=18, decimal_places=0)  # Field name made lowercase.
    legajo = models.DecimalField(db_column='Legajo', max_digits=18, decimal_places=0)  # Field name made lowercase.
    planilla = models.DecimalField(db_column='Planilla', max_digits=18, decimal_places=0)  # Field name made lowercase.
    renglon = models.AutoField(db_column='Renglon', primary_key=True)  # Field name made lowercase.
    caracter = models.CharField(db_column='Caracter', max_length=2)  # Field name made lowercase.
    cargo = models.ForeignKey('Categorias', on_delete=models.CASCADE, db_column='Cargo', blank=True, null=True)  # Field name made lowercase.
    fecha_desde = models.DateTimeField(db_column='Fecha Desde')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fecha_hasta = models.DateTimeField(db_column='Fecha Hasta')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    interrupcion = models.CharField(db_column='Interrupcion', max_length=1, blank=True, null=True)  # Field name made lowercase.
    jubilacion = models.CharField(db_column='Jubilacion', max_length=1, blank=True, null=True)  # Field name made lowercase.
    maternidad = models.CharField(db_column='Maternidad', max_length=1, blank=True, null=True)  # Field name made lowercase.
    porc_invalidez = models.DecimalField(db_column='Porc Invalidez', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    observacion = models.CharField(db_column='Observacion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dias = models.DecimalField(db_column='Dias', max_digits=18, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Certificaciones Servicios'
        unique_together = (('documento', 'legajo', 'planilla', 'renglon'),)


class Certificacionesht(models.Model):
    idd = models.AutoField(db_column='IDD',primary_key=True)  # Field name made lowercase.
    planilla = models.DecimalField(db_column='Planilla', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    documento = models.DecimalField(db_column='Documento', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    legajo = models.DecimalField(db_column='Legajo', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    fechaproceso = models.DateTimeField(db_column='FechaProceso', blank=True, null=True)  # Field name made lowercase.
    empresa = models.ForeignKey('Empresas', on_delete=models.CASCADE, db_column='Empresa', blank=True, null=True)  # Field name made lowercase.
    fechadesde = models.DateTimeField(db_column='FechaDesde', blank=True, null=True)  # Field name made lowercase.
    fechahasta = models.DateTimeField(db_column='FechaHasta', blank=True, null=True)  # Field name made lowercase.
    opccaja = models.CharField(db_column='OpcCaja', max_length=1, blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=200, blank=True, null=True)  # Field name made lowercase.
    prescripcion = models.IntegerField(db_column='Prescripcion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'CertificacionesHT'


class Conceptos(models.Model):
    idd_concepto = models.DecimalField(db_column='idd_Concepto', max_digits=18, decimal_places=0,primary_key=True)  # Field name made lowercase.
    empresa = models.CharField(db_column='Empresa', max_length=6)  # Field name made lowercase.
    concepto = models.CharField(db_column='Concepto', max_length=3)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=30)  # Field name made lowercase.
    grupo = models.CharField(max_length=2, blank=True, null=True)
    novedades = models.CharField(db_column='Novedades', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Conceptos'


class Dependencias(models.Model):
    codigo_dependencia = models.CharField(db_column='Codigo Dependencia', primary_key=True, max_length=3)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    descripcion_dependencia = models.CharField(db_column='Descripcion Dependencia', max_length=200)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    telefono = models.CharField(db_column='Telefono', max_length=50, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=200, blank=True, null=True)  # Field name made lowercase.
    localidad = models.CharField(db_column='Localidad', max_length=25, blank=True, null=True)  # Field name made lowercase.
    jurisdiccion = models.IntegerField(db_column='Jurisdiccion')  # Field name made lowercase.
    unidgest = models.IntegerField(db_column='UnidGest', blank=True, null=True)  # Field name made lowercase.
    activo = models.IntegerField(db_column='Activo')  # Field name made lowercase.
    dec_nro = models.IntegerField(db_column='Dec Nro')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dec_anio = models.IntegerField(db_column='Dec Anio')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    depsiga = models.IntegerField(db_column='DepSiga', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Dependencias'


class DescuentosSalarioFamiliar(models.Model):
    nroorden = models.AutoField(db_column='NroOrden', primary_key=True)  # Field name made lowercase.
    documento = models.DecimalField(db_column='Documento', max_digits=18, decimal_places=0)  # Field name made lowercase.
    legajo = models.DecimalField(db_column='Legajo', max_digits=18, decimal_places=0)  # Field name made lowercase.
    empresa = models.CharField(db_column='Empresa', max_length=6)  # Field name made lowercase.
    importe_total = models.DecimalField(db_column='Importe Total', max_digits=18, decimal_places=2)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    importe_cuota = models.DecimalField(db_column='Importe Cuota', max_digits=18, decimal_places=2)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fecha_carga = models.DateTimeField(db_column='Fecha Carga', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    usuario = models.CharField(db_column='Usuario', max_length=50, blank=True, null=True)  # Field name made lowercase.
    terminal = models.CharField(db_column='Terminal', max_length=15, blank=True, null=True)  # Field name made lowercase.
    concepto = models.IntegerField(db_column='Concepto')  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=3000, blank=True, null=True)  # Field name made lowercase.
    total_cancelar = models.DecimalField(db_column='Total Cancelar', max_digits=18, decimal_places=2)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    fecha_desde = models.DateTimeField(db_column='Fecha Desde', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fecha_hasta = models.DateTimeField(db_column='Fecha Hasta', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    indicador = models.IntegerField(db_column='Indicador')  # Field name made lowercase.
    dias = models.IntegerField(db_column='Dias', blank=True, null=True)  # Field name made lowercase.
    fecha_desdeaj = models.DateTimeField(db_column='Fecha DesdeAj', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fecha_hastaaj = models.DateTimeField(db_column='Fecha HastaAj', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cargo = models.CharField(db_column='Cargo', max_length=3, blank=True, null=True)  # Field name made lowercase.
    empajuste = models.CharField(db_column='EmpAjuste', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Descuentos Salario Familiar'
        unique_together = (('nroorden', 'documento', 'legajo', 'empresa', 'concepto'),)


class Empresas(models.Model):
    idd = models.AutoField(db_column='Idd', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=6)  # Field name made lowercase.
    detalle = models.CharField(db_column='Detalle', max_length=50, blank=True, null=True)  # Field name made lowercase.
    importe1 = models.CharField(max_length=50, blank=True, null=True)
    importe2 = models.CharField(max_length=50, blank=True, null=True)
    importe3 = models.CharField(max_length=50, blank=True, null=True)
    importe4 = models.CharField(max_length=50, blank=True, null=True)
    importe5 = models.CharField(max_length=50, blank=True, null=True)
    importe6 = models.CharField(max_length=50, blank=True, null=True)
    importe7 = models.CharField(max_length=50, blank=True, null=True)
    importe8 = models.CharField(max_length=50, blank=True, null=True)
    importe9 = models.CharField(max_length=50, blank=True, null=True)
    importe10 = models.CharField(max_length=50, blank=True, null=True)
    cambioescala = models.DateTimeField(db_column='CambioEscala', blank=True, null=True)  # Field name made lowercase.
    liquidacion = models.IntegerField(db_column='Liquidacion', blank=True, null=True)  # Field name made lowercase.
    acreditacion = models.IntegerField(db_column='Acreditacion', blank=True, null=True)  # Field name made lowercase.
    impagos = models.IntegerField(db_column='Impagos', blank=True, null=True)  # Field name made lowercase.
    antiguedad = models.IntegerField(db_column='Antiguedad', blank=True, null=True)  # Field name made lowercase.
    activos_sist = models.IntegerField(db_column='Activos_Sist', blank=True, null=True)  # Field name made lowercase.
    ayuda = models.IntegerField(db_column='Ayuda', blank=True, null=True)  # Field name made lowercase.
    letra = models.CharField(db_column='Letra', max_length=1, blank=True, null=True)  # Field name made lowercase.
    clasif_empresa = models.IntegerField(db_column='Clasif Empresa', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    contable = models.IntegerField(db_column='Contable', blank=True, null=True)  # Field name made lowercase.
    recibo_leyenda = models.CharField(db_column='Recibo_Leyenda', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Empresas'


class Legajos(models.Model):
    documento = models.DecimalField(db_column='Documento', primary_key=True, max_digits=18, decimal_places=0)  # Field name made lowercase.
    idd_legajos = models.DecimalField(max_digits=18, decimal_places=0)
    legajo = models.DecimalField(db_column='Legajo', max_digits=18, decimal_places=0)  # Field name made lowercase.
    empresa = models.CharField(db_column='Empresa', max_length=6)  # Field name made lowercase.
    fecha_proceso = models.DateTimeField(db_column='Fecha Proceso')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fecha_ingreso = models.DateTimeField(db_column='Fecha Ingreso', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fecha_egreso = models.DateTimeField(db_column='Fecha Egreso', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tipo_liquidacion = models.CharField(db_column='Tipo Liquidacion', max_length=2)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    categoria = models.CharField(db_column='Categoria', max_length=3, blank=True, null=True)  # Field name made lowercase.
    dependencia = models.CharField(db_column='Dependencia', max_length=3, blank=True, null=True)  # Field name made lowercase.
    antiguedad = models.DecimalField(db_column='Antiguedad', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=1)  # Field name made lowercase.
    caja_de_ahorro = models.CharField(db_column='Caja de Ahorro', max_length=9, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    poderes = models.CharField(db_column='Poderes', max_length=2, blank=True, null=True)  # Field name made lowercase.
    jurisdiccion = models.CharField(db_column='Jurisdiccion', max_length=2, blank=True, null=True)  # Field name made lowercase.
    secretarias = models.CharField(db_column='Secretarias', max_length=1, blank=True, null=True)  # Field name made lowercase.
    unidad_ejecutora = models.CharField(db_column='Unidad Ejecutora', max_length=2, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    subparcial = models.CharField(db_column='Subparcial', max_length=2, blank=True, null=True)  # Field name made lowercase.
    agrupamiento = models.CharField(db_column='Agrupamiento', max_length=2, blank=True, null=True)  # Field name made lowercase.
    situacion = models.CharField(db_column='Situacion', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Legajos'
        unique_together = (('documento', 'idd_legajos'),)


class Liquidacion(models.Model):
    documento = models.DecimalField(db_column='Documento', primary_key=True, max_digits=18, decimal_places=0)  # Field name made lowercase.
    idd_legajos = models.DecimalField(db_column='idd_Legajos', max_digits=18, decimal_places=0)  # Field name made lowercase.
    idd_concepto = models.DecimalField(db_column='idd_Concepto', max_digits=18, decimal_places=0)  # Field name made lowercase.
    orden = models.DecimalField(db_column='Orden', max_digits=18, decimal_places=0)  # Field name made lowercase.
    unidades = models.DecimalField(db_column='Unidades', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=18, decimal_places=2)  # Field name made lowercase.
    concepto1 = models.DecimalField(db_column='Concepto1', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    liq_horas = models.DecimalField(db_column='Liq_Horas', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    liq_escalas = models.DecimalField(db_column='Liq_Escalas', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    t1fecha = models.DateTimeField(db_column='T1fecha', blank=True, null=True)  # Field name made lowercase.
    t2fecha = models.DateTimeField(db_column='T2fecha', blank=True, null=True)  # Field name made lowercase.
    t3fecha = models.DateTimeField(db_column='T3fecha', blank=True, null=True)  # Field name made lowercase.
    liq_cargo = models.DecimalField(db_column='Liq_Cargo', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    t2numeric = models.DecimalField(db_column='T2numeric', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    t3numeric = models.DecimalField(db_column='T3numeric', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Liquidacion'
        unique_together = (('documento', 'idd_legajos', 'idd_concepto', 'orden'),)


class Maestro(models.Model):
    documento = models.DecimalField(db_column='Documento', max_digits=18, decimal_places=0)  # Field name made lowercase.
    legajo = models.DecimalField(db_column='Legajo', max_digits=18, decimal_places=0)  # Field name made lowercase.
    fecha_proceso = models.DateTimeField(db_column='Fecha Proceso')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    empresa = models.CharField(db_column='Empresa', max_length=6)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=1)  # Field name made lowercase.
    fecha_ingreso = models.DateTimeField(db_column='Fecha Ingreso', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fecha_egreso = models.CharField(db_column='Fecha Egreso', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dependencia = models.CharField(db_column='Dependencia', max_length=3)  # Field name made lowercase.
    cargo = models.CharField(db_column='Cargo', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cargo_reemplazo = models.CharField(db_column='Cargo Reemplazo', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cargo_retroactivo = models.CharField(db_column='Cargo Retroactivo', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cantidad_horas = models.DecimalField(db_column='Cantidad Horas', max_digits=18, decimal_places=0)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    antiguedad = models.DecimalField(db_column='Antiguedad', max_digits=18, decimal_places=0)  # Field name made lowercase.
    antiguedad_decreto = models.DecimalField(db_column='Antiguedad Decreto', max_digits=18, decimal_places=0)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    seguro_obligatorio = models.CharField(db_column='Seguro Obligatorio', max_length=1, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    seguro_familiar = models.CharField(db_column='Seguro Familiar', max_length=1, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    seguro_colectivo = models.CharField(db_column='Seguro Colectivo', max_length=1, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    maternidad_fecha_salida = models.CharField(db_column='Maternidad Fecha Salida', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    maternidad_total_dias = models.DecimalField(db_column='Maternidad Total Dias', max_digits=18, decimal_places=0)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    licencia = models.CharField(db_column='Licencia', max_length=1, blank=True, null=True)  # Field name made lowercase.
    sindicato_ate = models.CharField(db_column='Sindicato ATE', max_length=2, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sindicato_atsa = models.CharField(db_column='Sindicato ATSA', max_length=2, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sindicato_upcn = models.CharField(db_column='Sindicato UPCN', max_length=2, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dependencia_fisica = models.CharField(db_column='Dependencia Fisica', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    aporte_jubilatorio = models.DecimalField(db_column='Aporte Jubilatorio', max_digits=18, decimal_places=4)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sindicato_sat = models.CharField(db_column='Sindicato SAT', max_length=2, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    obra_social = models.CharField(db_column='Obra Social', max_length=2)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    obra_social_fam_cargo = models.DecimalField(db_column='Obra Social Fam Cargo', max_digits=18, decimal_places=0)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vacaciones_dias = models.DecimalField(db_column='Vacaciones Dias', max_digits=18, decimal_places=0)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    caja_complementaria = models.DecimalField(db_column='Caja Complementaria', max_digits=18, decimal_places=0)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    situacion_revista = models.CharField(db_column='Situacion Revista', max_length=1, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fecha_liquidacion = models.CharField(db_column='Fecha Liquidacion', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tarea = models.CharField(db_column='Tarea', max_length=1, blank=True, null=True)  # Field name made lowercase.
    legajo_historico = models.CharField(db_column='Legajo Historico', max_length=30, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    motivo_baja = models.CharField(db_column='Motivo Baja', max_length=2, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    derecho_ocupacion = models.DecimalField(db_column='Derecho Ocupacion', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    art = models.IntegerField(db_column='ART', blank=True, null=True)  # Field name made lowercase.
    idmaestro = models.AutoField(db_column='IDMaestro', primary_key=True)  # Field name made lowercase.
    origen = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Maestro'
        unique_together = (('documento', 'legajo', 'fecha_proceso', 'empresa'),)


class Parametros(models.Model):
    idd = models.AutoField(db_column='Idd', primary_key=True)
    registro = models.DecimalField(db_column='Registro', max_digits=18, decimal_places=0)  # Field name made lowercase.
    razon_social = models.CharField(db_column='Razon_social', max_length=200)  # Field name made lowercase.
    fecha_contrato = models.DateTimeField(db_column='Fecha_contrato', blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=100)  # Field name made lowercase.
    localidad = models.CharField(db_column='Localidad', max_length=50)  # Field name made lowercase.
    cp = models.CharField(max_length=10)
    cuit = models.CharField(db_column='Cuit', max_length=11)  # Field name made lowercase.
    caja_ahorro = models.CharField(db_column='Caja_ahorro', max_length=50)  # Field name made lowercase.
    fecha_tomasceses = models.DateTimeField(db_column='Fecha TomasCeses')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fecha_caja = models.DateTimeField(db_column='Fecha Caja', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fecha_maestro = models.DateTimeField(db_column='Fecha Maestro', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fecha_novedades = models.DateTimeField(db_column='Fecha Novedades', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fecha_familiares = models.DateTimeField(db_column='Fecha Familiares', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fecha_actualizacion = models.DateTimeField(db_column='Fecha Actualizacion', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    idd_legajo = models.DecimalField(db_column='Idd_Legajo', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    idd_concepto = models.DecimalField(db_column='Idd_Concepto', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    fecha_nula = models.DateTimeField(db_column='Fecha Nula', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fecha_pvdesde = models.DateTimeField(db_column='Fecha PVdesde', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fecha_pvhasta = models.DateTimeField(db_column='Fecha PVhasta', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fecha_texto = models.CharField(db_column='Fecha texto', max_length=8, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cuotas_sac = models.IntegerField(db_column='Cuotas SAC', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    valor_ind_prov = models.DecimalField(db_column='Valor Ind. Prov', max_digits=18, decimal_places=5, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    valor_ind_nac = models.DecimalField(db_column='Valor Ind. Nac', max_digits=18, decimal_places=5, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nro_recibo = models.DecimalField(db_column='Nro_Recibo', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    fecha_compl = models.DateTimeField(db_column='Fecha Compl', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cuota_compl = models.IntegerField(db_column='Cuota Compl', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cuota_ayuda = models.IntegerField(db_column='Cuota Ayuda', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nro_certificado = models.DecimalField(db_column='Nro_Certificado', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    topesalarial = models.DecimalField(db_column='TopeSalarial', max_digits=18, decimal_places=2)  # Field name made lowercase.
    fecha_sac_desde = models.DateTimeField(db_column='Fecha SAC Desde', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fecha_sac_hasta = models.DateTimeField(db_column='Fecha SAC Hasta', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    versiontercop = models.CharField(db_column='VersionTercop', max_length=10, blank=True, null=True)  # Field name made lowercase.
    versionliquidador = models.CharField(db_column='VersionLiquidador', max_length=10, blank=True, null=True)  # Field name made lowercase.
    leyenda = models.CharField(db_column='Leyenda', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sueldo_vital = models.DecimalField(db_column='Sueldo Vital', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ltpasantes = models.IntegerField(db_column='LTPasantes', blank=True, null=True)  # Field name made lowercase.
    fdesdefojpol = models.DateTimeField(db_column='FDesdeFojPol', blank=True, null=True)  # Field name made lowercase.
    fhastafojpol = models.DateTimeField(db_column='FHastaFojPol', blank=True, null=True)  # Field name made lowercase.
    fechasrecpol = models.CharField(db_column='FechasRecPol', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fechacierresistema = models.DateTimeField(db_column='FechaCierreSistema', blank=True, null=True)  # Field name made lowercase.
    identidad = models.DecimalField(max_digits=18, decimal_places=0)
    fdesdelic34pol = models.DateTimeField(db_column='FdesdeLic34Pol', blank=True, null=True)  # Field name made lowercase.
    fhastalic34pol = models.DateTimeField(db_column='FhastaLic34Pol', blank=True, null=True)  # Field name made lowercase.
    art = models.DecimalField(db_column='ART', max_digits=18, decimal_places=2)  # Field name made lowercase.
    coeficiente_art = models.DecimalField(db_column='Coeficiente_art', max_digits=18, decimal_places=6)  # Field name made lowercase.
    tope_minimo_art = models.DecimalField(db_column='Tope_Minimo_art', max_digits=18, decimal_places=2)  # Field name made lowercase.
    tope_maximo_art = models.DecimalField(db_column='Tope_maximo_art', max_digits=18, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Parametros'


class Personas(models.Model):
    id = models.AutoField(primary_key=True)
    documento = models.DecimalField(db_column='Documento', max_digits=18, decimal_places=0)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=80)  # Field name made lowercase.
    apellidosolo = models.CharField(db_column='apellidoSolo', max_length=40)  # Field name made lowercase.
    nombre = models.CharField(max_length=40)
    domicilio = models.CharField(db_column='Domicilio', max_length=100, blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(max_length=30)
    email = models.CharField(max_length=80)
    localidad = models.CharField(db_column='Localidad', max_length=12, blank=True, null=True)  # Field name made lowercase.
    fecha_de_nacimiento = models.DateTimeField(db_column='Fecha de Nacimiento', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    id_cuenta = models.DecimalField(max_digits=18, decimal_places=0)
    caja_de_ahorro = models.CharField(db_column='Caja de Ahorro', max_length=9, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sexo = models.CharField(db_column='Sexo', max_length=1, blank=True, null=True)  # Field name made lowercase.
    imagen = models.BinaryField(db_column='Imagen', blank=True, null=True)  # Field name made lowercase.
    cuil0 = models.CharField(db_column='Cuil0', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cuil1 = models.CharField(db_column='Cuil1', max_length=1, blank=True, null=True)  # Field name made lowercase.
    aporte_solidario = models.DecimalField(db_column='Aporte Solidario', max_digits=18, decimal_places=2)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    psicofisicos_fecha = models.DateTimeField(db_column='Psicofisicos fecha', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    psicofisicos_condicion = models.IntegerField(db_column='Psicofisicos condicion', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    psicofisicos_duracion = models.IntegerField(db_column='Psicofisicos duracion', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cbuena_salud_fecha = models.DateTimeField(db_column='CBuena Salud Fecha', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cbuena_salud_condicion = models.IntegerField(db_column='CBuena Salud Condicion', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    creincidencia_fecha = models.DateTimeField(db_column='CReincidencia fecha', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    creincidencia_condicion = models.IntegerField(db_column='CReincidencia Condicion', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cbu = models.CharField(db_column='CBU', max_length=22, blank=True, null=True)  # Field name made lowercase.
    const_patrimonial_desde = models.DateTimeField(db_column='Const Patrimonial Desde', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    const_patrimonial_hasta = models.DateTimeField(db_column='Const Patrimonial Hasta', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    const_patrimonial_condicion = models.IntegerField(db_column='Const Patrimonial Condicion', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    origen = models.CharField(max_length=6)

    class Meta:
        managed = True
        db_table = 'Personas'


class ReemplazoAplicativos(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    aplicacion = models.CharField(max_length=50)
    killer = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'Reemplazo_aplicativos'


class RptCtrolcertgiradas(models.Model):
    idd = models.AutoField(db_column='Idd', primary_key=True)
    orden = models.CharField(max_length=1)
    leyenda = models.CharField(max_length=88)
    documento = models.DecimalField(db_column='Documento', max_digits=18, decimal_places=0)  # Field name made lowercase.
    legajo = models.DecimalField(db_column='Legajo', max_digits=18, decimal_places=0)  # Field name made lowercase.
    planilla = models.DecimalField(db_column='Planilla', max_digits=18, decimal_places=0)  # Field name made lowercase.
    apellido = models.CharField(max_length=80)
    empresa = models.CharField(db_column='Empresa', max_length=6, blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fecha_pedido = models.DateTimeField(db_column='Fecha Pedido', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    causa = models.CharField(db_column='Causa', max_length=45, blank=True, null=True)  # Field name made lowercase.
    causa_cesacion = models.CharField(db_column='Causa Cesacion', max_length=600, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fecha_cesacion = models.DateTimeField(db_column='Fecha Cesacion', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fecha_pase_rh = models.DateTimeField(db_column='Fecha Pase RH', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fecha_pase_dgh = models.DateTimeField(db_column='Fecha Pase DGH', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    deuda = models.IntegerField()
    valorizacion = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'Rpt_CtrolCertGiradas'



class Tmpcpt(models.Model):
    empresa = models.CharField(db_column='Empresa', primary_key=True, max_length=6)  # Field name made lowercase.
    concepto = models.IntegerField(db_column='Concepto')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=60)  # Field name made lowercase.
    descripcion_completa = models.CharField(db_column='Descripcion Completa', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    importe1 = models.DecimalField(db_column='Importe1', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    importe2 = models.DecimalField(db_column='Importe2', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    novedades = models.IntegerField(db_column='Novedades', blank=True, null=True)  # Field name made lowercase.
    cargo = models.IntegerField(db_column='Cargo', blank=True, null=True)  # Field name made lowercase.
    dias = models.IntegerField(db_column='Dias', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='Cantidad', blank=True, null=True)  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    radicacion = models.IntegerField(db_column='Radicacion', blank=True, null=True)  # Field name made lowercase.
    imputacion = models.CharField(db_column='Imputacion', max_length=10, blank=True, null=True)  # Field name made lowercase.
    grupo = models.IntegerField(db_column='Grupo')  # Field name made lowercase.
    subgrupo = models.IntegerField(db_column='Subgrupo', blank=True, null=True)  # Field name made lowercase.
    fecha_desde = models.DateTimeField(db_column='Fecha Desde')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fecha_hasta = models.DateTimeField(db_column='Fecha Hasta', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    activo = models.IntegerField(db_column='Activo')  # Field name made lowercase.
    subgrupo2 = models.IntegerField(db_column='SubGrupo2', blank=True, null=True)  # Field name made lowercase.
    ipauss = models.IntegerField()
    cajacoeficiente = models.IntegerField(db_column='CajaCoeficiente', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Tmpcpt'
        unique_together = (('empresa', 'concepto'),)


class TomasCesesAdm(models.Model):
    documento = models.DecimalField(db_column='Documento', max_digits=18, decimal_places=0)  # Field name made lowercase.
    legajo = models.DecimalField(db_column='Legajo', max_digits=18, decimal_places=0)  # Field name made lowercase.
    idd_tomas = models.AutoField(db_column='Idd_Tomas', primary_key=True)  # Field name made lowercase.
    fecha_desde = models.DateTimeField(db_column='Fecha Desde')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fecha_hasta = models.CharField(db_column='Fecha hasta', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dependencia = models.CharField(db_column='Dependencia', max_length=3)  # Field name made lowercase.
    categoria = models.ForeignKey('Categorias', on_delete=models.CASCADE, db_column='Categoria')  # Field name made lowercase.
    agrupamiento = models.IntegerField(db_column='Agrupamiento')  # Field name made lowercase.
    planta = models.IntegerField(db_column='Planta')  # Field name made lowercase.
    responsabilidad = models.CharField(db_column='Responsabilidad', max_length=3, blank=True, null=True)  # Field name made lowercase.
    clasificacion = models.CharField(db_column='Clasificacion', max_length=5, blank=True, null=True)  # Field name made lowercase.
    fecha_liquidacion = models.CharField(db_column='Fecha Liquidacion', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    instr_tip1 = models.CharField(db_column='Instr_Tip1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    instr_nro1 = models.IntegerField(db_column='Instr_Nro1', blank=True, null=True)  # Field name made lowercase.
    instr_ano1 = models.IntegerField(db_column='Instr_Ano1', blank=True, null=True)  # Field name made lowercase.
    instr_let1 = models.CharField(db_column='Instr_Let1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    instr_tip2 = models.CharField(db_column='Instr_Tip2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    instr_nro2 = models.IntegerField(db_column='Instr_Nro2', blank=True, null=True)  # Field name made lowercase.
    instr_ano2 = models.IntegerField(db_column='Instr_Ano2', blank=True, null=True)  # Field name made lowercase.
    instr_let2 = models.CharField(db_column='Instr_Let2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=300, blank=True, null=True)  # Field name made lowercase.
    tca_usuario = models.CharField(db_column='TCA_Usuario', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tca_terminal = models.CharField(db_column='TCA_Terminal', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tca_fecha = models.DateTimeField(db_column='TCA_Fecha', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Tomas_Ceses_Adm'
        unique_together = (('documento', 'legajo', 'idd_tomas'),)


class UserHome(models.Model):
    idd = models.AutoField(db_column='IDD', primary_key=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=50, blank=True, null=True)  # Field name made lowercase.
    home = models.CharField(db_column='Home', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sector = models.CharField(db_column='Sector', max_length=15, blank=True, null=True)  # Field name made lowercase.
    dependencia = models.CharField(db_column='Dependencia', max_length=2, blank=True, null=True)  # Field name made lowercase.
    area = models.IntegerField(db_column='Area')  # Field name made lowercase.
    nombre_y_apellido = models.CharField(db_column='Nombre y Apellido', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cargo = models.CharField(db_column='Cargo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ministerio = models.CharField(db_column='Ministerio', max_length=50, blank=True, null=True)  # Field name made lowercase.
    certificacionesyservicios = models.IntegerField(db_column='CertificacionesyServicios')  # Field name made lowercase.
    home_user = models.CharField(max_length=30, blank=True, null=True)
    home_password = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'User Home'


class Valorizaciones(models.Model):
    idd_val = models.AutoField(db_column='IDD_Val', primary_key=True)  # Field name made lowercase.
    documento = models.DecimalField(db_column='Documento', max_digits=18, decimal_places=0)  # Field name made lowercase.
    legajo = models.DecimalField(db_column='Legajo', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    empresa = models.CharField(db_column='Empresa', max_length=6)  # Field name made lowercase.
    nro_notarh = models.CharField(db_column='Nro NotaRH', max_length=15, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fecha_entrada_rh = models.DateTimeField(db_column='Fecha Entrada RH', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nro_notadgh = models.CharField(db_column='Nro NotaDGH', max_length=15, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fecha_salida_dgh = models.DateTimeField(db_column='Fecha Salida DGH', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    deposito = models.CharField(db_column='Deposito', max_length=15, blank=True, null=True)  # Field name made lowercase.
    fecha_deposito = models.DateTimeField(db_column='Fecha Deposito', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    observaciones = models.TextField(db_column='Observaciones', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    anulado = models.CharField(db_column='Anulado', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cancelado = models.CharField(db_column='Cancelado', max_length=1, blank=True, null=True)  # Field name made lowercase.
    prescripto = models.IntegerField(db_column='Prescripto', blank=True, null=True)  # Field name made lowercase.
    importe_bruto = models.DecimalField(max_digits=18, decimal_places=4)
    importe_liquido = models.DecimalField(max_digits=18, decimal_places=4)
    novedad_negativa = models.CharField(max_length=2500)

    class Meta:
        managed = True
        db_table = 'Valorizaciones'
    def __str__(self):
        return self.field_name


class Categorias(models.Model):
    idd = models.AutoField(db_column='Idd', primary_key=True)
    decreto = models.CharField(db_column='Decreto', max_length=30)  # Field name made lowercase.
    fecha_vig = models.DateTimeField(db_column='Fecha Vig')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    categoria = models.CharField(db_column='Categoria', max_length=3)  # Field name made lowercase.
    empresa = models.CharField(db_column='Empresa', max_length=6)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=200, blank=True, null=True)  # Field name made lowercase.
    secuencia = models.DecimalField(db_column='Secuencia', max_digits=18, decimal_places=2)  # Field name made lowercase.
    jerarquia_relacionada = models.CharField(db_column='Jerarquia Relacionada', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ubicacion = models.DecimalField(db_column='Ubicacion', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    importe1 = models.DecimalField(db_column='Importe1', max_digits=18, decimal_places=2)  # Field name made lowercase.
    importe2 = models.DecimalField(db_column='Importe2', max_digits=18, decimal_places=2)  # Field name made lowercase.
    importe3 = models.DecimalField(db_column='Importe3', max_digits=18, decimal_places=2)  # Field name made lowercase.
    importe4 = models.DecimalField(db_column='Importe4', max_digits=18, decimal_places=2)  # Field name made lowercase.
    importe5 = models.DecimalField(db_column='Importe5', max_digits=18, decimal_places=2)  # Field name made lowercase.
    importe6 = models.DecimalField(db_column='Importe6', max_digits=18, decimal_places=2)  # Field name made lowercase.
    importe7 = models.DecimalField(db_column='Importe7', max_digits=18, decimal_places=2)  # Field name made lowercase.
    importe8 = models.DecimalField(db_column='Importe8', max_digits=18, decimal_places=2)  # Field name made lowercase.
    importe9 = models.DecimalField(db_column='Importe9', max_digits=18, decimal_places=2)  # Field name made lowercase.
    importe10 = models.DecimalField(db_column='Importe10', max_digits=18, decimal_places=2)  # Field name made lowercase.
    porc_asistencia = models.DecimalField(db_column='Porc. Asistencia', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    escalanro = models.IntegerField(db_column='EscalaNro', blank=True, null=True)  # Field name made lowercase.
    horas = models.DecimalField(db_column='Horas', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    horasdetalle = models.CharField(db_column='HorasDetalle', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'categorias'


class CertificacionesJubdocente(models.Model):
    idd = models.AutoField(db_column='Idd', primary_key=True)
    anio = models.IntegerField(db_column='Anio')  # Field name made lowercase.
    edadmujer = models.IntegerField(db_column='EdadMujer')  # Field name made lowercase.
    edadhombre = models.IntegerField(db_column='EdadHombre')  # Field name made lowercase.
    aniosmujer = models.IntegerField(db_column='AniosMujer')  # Field name made lowercase.
    anioshombre = models.IntegerField(db_column='AniosHombre')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'certificaciones jubdocente'


class CertificacionesJubedadavanzada(models.Model):
    idd = models.AutoField(db_column='Idd', primary_key=True)
    anio = models.IntegerField(db_column='Anio')  # Field name made lowercase.
    edadmujer = models.IntegerField(db_column='EdadMujer')  # Field name made lowercase.
    edadhombre = models.IntegerField(db_column='EdadHombre')  # Field name made lowercase.
    aniosmujer = models.IntegerField(db_column='AniosMujer')  # Field name made lowercase.
    anioshombre = models.IntegerField(db_column='AniosHombre')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'certificaciones jubedadavanzada'


class Seguridad(models.Model):
    usuario = models.CharField(db_column='Usuario', primary_key=True, max_length=50)  # Field name made lowercase.
    clave = models.BinaryField(db_column='Clave')  # Field name made lowercase.
    dependencia = models.CharField(db_column='Dependencia', max_length=2, blank=True, null=True)  # Field name made lowercase.
    personal = models.CharField(db_column='Personal', max_length=1, blank=True, null=True)  # Field name made lowercase.
    empresa = models.CharField(db_column='Empresa', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tomas_ceses = models.CharField(db_column='Tomas Ceses', max_length=1, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    caja_ahorro = models.CharField(db_column='Caja Ahorro', max_length=1, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sistemas = models.CharField(db_column='Sistemas', max_length=1, blank=True, null=True)  # Field name made lowercase.
    familiares = models.CharField(db_column='Familiares', max_length=1, blank=True, null=True)  # Field name made lowercase.
    certificaciones = models.CharField(db_column='Certificaciones', max_length=1, blank=True, null=True)  # Field name made lowercase.
    documento = models.CharField(db_column='Documento', max_length=1, blank=True, null=True)  # Field name made lowercase.
    planta_presupuesto = models.CharField(db_column='Planta Presupuesto', max_length=1, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mesa = models.CharField(db_column='Mesa', max_length=1, blank=True, null=True)  # Field name made lowercase.
    recibos = models.CharField(db_column='Recibos', max_length=1, blank=True, null=True)  # Field name made lowercase.
    buscador = models.CharField(db_column='Buscador', max_length=1, blank=True, null=True)  # Field name made lowercase.
    desafectaciones = models.CharField(db_column='Desafectaciones', max_length=1, blank=True, null=True)  # Field name made lowercase.
    asistencia = models.CharField(db_column='Asistencia', max_length=1, blank=True, null=True)  # Field name made lowercase.
    secos = models.CharField(db_column='Secos', max_length=1, blank=True, null=True)  # Field name made lowercase.
    salud = models.CharField(db_column='Salud', max_length=1, blank=True, null=True)  # Field name made lowercase.
    sat = models.CharField(db_column='Sat', max_length=1, blank=True, null=True)  # Field name made lowercase.
    aero = models.CharField(db_column='Aero', max_length=1, blank=True, null=True)  # Field name made lowercase.
    docpri = models.CharField(db_column='DocPri', max_length=1, blank=True, null=True)  # Field name made lowercase.
    docsec = models.CharField(db_column='DocSec', max_length=1, blank=True, null=True)  # Field name made lowercase.
    habilitacion = models.CharField(db_column='Habilitacion', max_length=1, blank=True, null=True)  # Field name made lowercase.
    consulta = models.CharField(db_column='Consulta', max_length=1, blank=True, null=True)  # Field name made lowercase.
    policia = models.CharField(db_column='Policia', max_length=1, blank=True, null=True)  # Field name made lowercase.
    planes = models.CharField(db_column='Planes', max_length=1, blank=True, null=True)  # Field name made lowercase.
    patronato = models.CharField(db_column='Patronato', max_length=1, blank=True, null=True)  # Field name made lowercase.
    liqpaplepra = models.CharField(db_column='LiqPAPLEPRA', max_length=1, blank=True, null=True)  # Field name made lowercase.
    auditor = models.CharField(db_column='Auditor', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ctrl_recibos = models.CharField(db_column='Ctrl Recibos', max_length=1, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    contratos = models.CharField(db_column='Contratos', max_length=1, blank=True, null=True)  # Field name made lowercase.
    retenciones = models.CharField(db_column='Retenciones', max_length=1, blank=True, null=True)  # Field name made lowercase.
    maquinas = models.CharField(db_column='Maquinas', max_length=1, blank=True, null=True)  # Field name made lowercase.
    sector = models.CharField(db_column='Sector', max_length=1, blank=True, null=True)  # Field name made lowercase.
    categorias = models.CharField(db_column='Categorias', max_length=1, blank=True, null=True)  # Field name made lowercase.
    subsidio = models.CharField(db_column='Subsidio', max_length=1, blank=True, null=True)  # Field name made lowercase.
    conceptos = models.CharField(db_column='Conceptos', max_length=1, blank=True, null=True)  # Field name made lowercase.
    aguinaldo = models.CharField(db_column='Aguinaldo', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ministerio = models.CharField(db_column='Ministerio', max_length=2, blank=True, null=True)  # Field name made lowercase.
    procesos = models.CharField(db_column='Procesos', max_length=1, blank=True, null=True)  # Field name made lowercase.
    segeducacion = models.IntegerField(db_column='SegEducacion', blank=True, null=True)  # Field name made lowercase.
    certificado = models.CharField(db_column='Certificado', max_length=1, blank=True, null=True)  # Field name made lowercase.
    consultmesaentrada = models.CharField(db_column='ConsultMesaEntrada', max_length=1, blank=True, null=True)  # Field name made lowercase.
    seguros = models.CharField(db_column='Seguros', max_length=1, blank=True, null=True)  # Field name made lowercase.
    vialidad = models.CharField(db_column='Vialidad', max_length=1, blank=True, null=True)  # Field name made lowercase.
    pel = models.CharField(db_column='Pel', max_length=1, blank=True, null=True)  # Field name made lowercase.
    alta_personas = models.CharField(db_column='Alta Personas', max_length=1, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    codigo_dependencia = models.CharField(db_column='Codigo Dependencia', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    segart = models.CharField(db_column='SegArt', max_length=1, blank=True, null=True)  # Field name made lowercase.
    valorizacion = models.CharField(db_column='Valorizacion', max_length=1, blank=True, null=True)  # Field name made lowercase.
    epu = models.CharField(db_column='Epu', max_length=1, blank=True, null=True)  # Field name made lowercase.
    retiro = models.CharField(db_column='Retiro', max_length=1, blank=True, null=True)  # Field name made lowercase.
    guardiashsextras = models.CharField(db_column='GuardiasHsExtras', max_length=1, blank=True, null=True)  # Field name made lowercase.
    grupos = models.CharField(db_column='Grupos', max_length=1)  # Field name made lowercase.
    salcap = models.CharField(db_column='Salcap', max_length=1)  # Field name made lowercase.
    polciv = models.CharField(db_column='Polciv', max_length=1, blank=True, null=True)  # Field name made lowercase.
    judiciales = models.CharField(db_column='Judiciales', max_length=1, blank=True, null=True)  # Field name made lowercase.
    penit = models.CharField(db_column='Penit', max_length=1, blank=True, null=True)  # Field name made lowercase.
    listados = models.CharField(db_column='Listados', max_length=1, blank=True, null=True)  # Field name made lowercase.
    impresion = models.CharField(db_column='Impresion', max_length=1, blank=True, null=True)  # Field name made lowercase.
    artpolicia = models.CharField(db_column='ArtPolicia', max_length=1, blank=True, null=True)  # Field name made lowercase.
    segdependencia = models.CharField(db_column='SegDependencia', max_length=1, blank=True, null=True)  # Field name made lowercase.
    segcertif = models.CharField(db_column='SegCertif', max_length=1, blank=True, null=True)  # Field name made lowercase.
    localidad = models.CharField(db_column='Localidad', max_length=2)  # Field name made lowercase.
    generaarchivo = models.CharField(db_column='GeneraArchivo', max_length=1)  # Field name made lowercase.
    polcaj = models.CharField(db_column='Polcaj', max_length=1, blank=True, null=True)  # Field name made lowercase.
    abm_usuario = models.CharField(db_column='ABM_Usuario', max_length=1, blank=True, null=True)  # Field name made lowercase.
    abm_procedimiento = models.CharField(db_column='ABM_procedimiento', max_length=1, blank=True, null=True)  # Field name made lowercase.
    segcontable = models.CharField(db_column='SegContable', max_length=1)  # Field name made lowercase.
    especial_usuario = models.CharField(db_column='Especial_Usuario', max_length=1)  # Field name made lowercase.
    teripauss = models.CharField(db_column='terIpauss', max_length=1, blank=True, null=True)  # Field name made lowercase.
    segsaludeduca = models.CharField(db_column='SegSaludEduca', max_length=1, blank=True, null=True)  # Field name made lowercase.
    correo = models.CharField(max_length=1)
    preocupacional = models.CharField(max_length=1)
    liq_docente = models.CharField(max_length=1)
    email = models.CharField(max_length=80)
    sysasistencia = models.CharField(db_column='sysAsistencia', max_length=1)  # Field name made lowercase.
    liq_administracion = models.CharField(max_length=1)
    rdp = models.CharField(max_length=1)
    dni = models.CharField(max_length=8, blank=True, null=True)
    id_sector = models.DecimalField(max_digits=18, decimal_places=0)
    rh_remuneracion = models.CharField(max_length=1)
    rendicion_disca = models.CharField(max_length=1)
    rendicion_vejez = models.CharField(max_length=1)
    liquidador = models.CharField(max_length=1)
    tercop = models.CharField(max_length=1)
    tercopweb = models.CharField(max_length=1)
    dir_trabajo = models.CharField(max_length=50)
    auditor_certif = models.CharField(max_length=1)
    perfilusuarioid = models.IntegerField(db_column='PerfilUsuarioID')  # Field name made lowercase.
    bandejasige = models.CharField(db_column='bandejaSige', max_length=1)  # Field name made lowercase.
    estadistica = models.CharField(max_length=1)

    class Meta:
        managed = True
        db_table = 'seguridad'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)




