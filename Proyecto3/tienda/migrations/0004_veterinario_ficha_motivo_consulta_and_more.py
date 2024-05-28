# Generated by Django 5.0.6 on 2024-05-28 18:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0003_delete_edad_delete_peso_remove_ficha_veterinario_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Veterinario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='ficha',
            name='motivo_consulta',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ficha',
            name='observaciones',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mascota',
            name='edad',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mascota',
            name='raza',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='mascota',
            name='sexo',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='ficha',
            name='veterinario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tienda.veterinario'),
        ),
    ]
