# Generated by Django 3.2.7 on 2021-10-27 03:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('senttevaluationapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleadoeliminado',
            name='Contraseña',
        ),
        migrations.RemoveField(
            model_name='empleadoeliminado',
            name='Rol',
        ),
    ]
