# Generated by Django 3.2.7 on 2021-10-24 21:59

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rut', models.CharField(max_length=12, unique=True, validators=[django.core.validators.RegexValidator(regex='^(\\d{1,3}(?:.\\d{1,3}){2}-[\\dkK])$')])),
                ('Nombre', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Z]')])),
                ('FechaIngreso', models.DateField()),
                ('Correo', models.CharField(max_length=100, unique=True, validators=[django.core.validators.EmailValidator])),
            ],
        ),
        migrations.CreateModel(
            name='EmpleadoEliminado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rut', models.CharField(max_length=12)),
                ('Nombre', models.CharField(max_length=50)),
                ('Contraseña', models.CharField(max_length=50)),
                ('Rol', models.CharField(max_length=50)),
                ('Correo', models.CharField(max_length=50)),
                ('FechaEliminacion', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gerencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreGerencia', models.CharField(max_length=50, unique=True, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Z]')])),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombrePerfil', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Z]')])),
            ],
        ),
        migrations.CreateModel(
            name='PlanAccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Accion', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Z]')])),
                ('Medicion', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Z]')])),
            ],
        ),
        migrations.CreateModel(
            name='SubGerencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreSubgerencia', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Z]')])),
                ('IdGerencia', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='senttevaluationapp.gerencia')),
            ],
        ),
        migrations.CreateModel(
            name='PerfilRol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rol', models.IntegerField(choices=[(1, 'Evaluador'), (2, 'Evaluado'), (3, 'Calibrador')], default=1)),
                ('RelacionEvaluado', models.CharField(blank=True, default='', max_length=50, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Z]')])),
                ('NombreEvaluador', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('NombreCalibrador', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('IdEmpleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='senttevaluationapp.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Evaluacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Estado', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Z]')])),
                ('Fase', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Z]')])),
                ('ComentarioCalibrador', models.CharField(max_length=80, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Z]')])),
                ('IdEmpleado', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='senttevaluationapp.empleado')),
            ],
        ),
        migrations.AddField(
            model_name='empleado',
            name='IdPerfil',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='senttevaluationapp.perfil'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='IdSubGerencia',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='senttevaluationapp.subgerencia'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='DetalleEv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FechaEvaluacion', models.DateField()),
                ('ComentarioEvaluador', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Z]')])),
                ('Calificacion', models.IntegerField(validators=[django.core.validators.RegexValidator(regex='^[0-9]')])),
                ('AutoEvaluacion', models.IntegerField(validators=[django.core.validators.RegexValidator(regex='^[0-9]')])),
                ('IdEvaluacion', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='senttevaluationapp.evaluacion')),
                ('IdPlanAccion', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='senttevaluationapp.planaccion')),
            ],
        ),
        migrations.CreateModel(
            name='Competencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreCompetencia', models.CharField(max_length=60, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Z]')])),
                ('Definicion', models.CharField(max_length=1000, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Z]')])),
                ('IdPerfil', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='senttevaluationapp.perfil')),
            ],
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreCargo', models.CharField(max_length=50, unique=True, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Z]')])),
                ('IdPerfil', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='senttevaluationapp.perfil')),
            ],
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreArea', models.CharField(max_length=50, unique=True, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Z]')])),
                ('IdGerencia', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='senttevaluationapp.gerencia')),
            ],
        ),
        migrations.CreateModel(
            name='AccionClave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descripcion', models.CharField(max_length=1000, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Z]')])),
                ('IdCompetencia', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='senttevaluationapp.competencia')),
            ],
        ),
    ]
