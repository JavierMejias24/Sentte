# Generated by Django 3.2.7 on 2021-10-24 21:28

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('senttevaluationapp', '0007_remove_competencia_idperfil'),
    ]

    operations = [
        migrations.AddField(
            model_name='competencia',
            name='IdPerfil',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='senttevaluationapp.perfil'),
        ),
        migrations.AlterField(
            model_name='competencia',
            name='NombreCompetencia',
            field=models.CharField(max_length=60, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Z]')]),
        ),
        migrations.DeleteModel(
            name='PerfilComp',
        ),
    ]