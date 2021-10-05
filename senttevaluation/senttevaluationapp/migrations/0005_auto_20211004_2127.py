# Generated by Django 3.2.7 on 2021-10-05 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('senttevaluationapp', '0004_auto_20211004_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='Rol',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='perfilrol',
            name='NombreCalibrador',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='perfilrol',
            name='NombreEvaluador',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='perfilrol',
            name='Rol',
            field=models.CharField(choices=[(1, 'Evaluador'), (2, 'Evaluado'), (3, 'Calibrador')], default=1, max_length=200),
        ),
    ]
