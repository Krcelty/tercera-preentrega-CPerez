# Generated by Django 5.0.6 on 2024-05-29 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0009_rename_motivo_consulta_ficha_consulta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ficha',
            name='id',
        ),
        migrations.AlterField(
            model_name='ficha',
            name='numero_ficha',
            field=models.PositiveIntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
