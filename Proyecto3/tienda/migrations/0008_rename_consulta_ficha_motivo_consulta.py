# Generated by Django 5.0.6 on 2024-05-28 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0007_rename_motivo_consulta_ficha_consulta'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ficha',
            old_name='consulta',
            new_name='motivo_consulta',
        ),
    ]
