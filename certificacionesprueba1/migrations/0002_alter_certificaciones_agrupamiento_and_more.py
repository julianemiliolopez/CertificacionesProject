# Generated by Django 4.0.7 on 2022-10-05 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('certificacionesprueba1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificaciones',
            name='agrupamiento',
            field=models.ForeignKey(blank=True, db_column='Agrupamiento', null=True, on_delete=django.db.models.deletion.CASCADE, to='certificacionesprueba1.agrupamientos'),
        ),
        migrations.AlterField(
            model_name='certificaciones',
            name='cargo',
            field=models.ForeignKey(blank=True, db_column='Cargo', null=True, on_delete=django.db.models.deletion.CASCADE, to='certificacionesprueba1.categorias'),
        ),
        migrations.AlterField(
            model_name='certificaciones',
            name='causa',
            field=models.ForeignKey(blank=True, db_column='Causa', null=True, on_delete=django.db.models.deletion.CASCADE, to='certificacionesprueba1.certificacionescausas'),
        ),
        migrations.AlterField(
            model_name='certificaciones',
            name='empresa',
            field=models.ForeignKey(blank=True, db_column='Empresa', null=True, on_delete=django.db.models.deletion.CASCADE, to='certificacionesprueba1.empresas'),
        ),
        migrations.AlterField(
            model_name='certificacionesht',
            name='empresa',
            field=models.ForeignKey(blank=True, db_column='Empresa', null=True, on_delete=django.db.models.deletion.CASCADE, to='certificacionesprueba1.empresas'),
        ),
        migrations.AlterField(
            model_name='certificacionespedidos',
            name='empresa',
            field=models.ForeignKey(db_column='Empresa', on_delete=django.db.models.deletion.CASCADE, to='certificacionesprueba1.empresas'),
        ),
        migrations.AlterField(
            model_name='certificacionespedidos',
            name='estado',
            field=models.ForeignKey(db_column='Estado', on_delete=django.db.models.deletion.CASCADE, to='certificacionesprueba1.certificacionesestados'),
        ),
        migrations.AlterField(
            model_name='certificacionesservicios',
            name='cargo',
            field=models.ForeignKey(blank=True, db_column='Cargo', null=True, on_delete=django.db.models.deletion.CASCADE, to='certificacionesprueba1.categorias'),
        ),
        migrations.AlterField(
            model_name='tomascesesadm',
            name='categoria',
            field=models.ForeignKey(db_column='Categoria', on_delete=django.db.models.deletion.CASCADE, to='certificacionesprueba1.categorias'),
        ),
    ]
