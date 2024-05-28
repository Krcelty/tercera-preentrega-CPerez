# Generated by Django 5.0.6 on 2024-05-28 20:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0005_veterinario_motivo_consulta_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='ficha',
            name='veterinario',
        ),
        migrations.RemoveField(
            model_name='ficha',
            name='observaciones',
        ),
        migrations.AlterField(
            model_name='ficha',
            name='motivo_consulta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tienda.consulta'),
        ),
        migrations.DeleteModel(
            name='Veterinario',
        ),
    ]
