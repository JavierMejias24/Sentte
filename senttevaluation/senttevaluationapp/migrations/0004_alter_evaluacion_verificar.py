# Generated by Django 3.2.7 on 2021-11-22 23:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('senttevaluationapp', '0003_auto_20211122_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluacion',
            name='verificar',
            field=models.CharField(blank=True, choices=[(1, 'Si'), (2, 'No')], default=1, max_length=50, null=True, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Z]')]),
        ),
    ]
