from django import forms
from . import  models


class MascotaForm(forms.ModelForm):
    nueva_mascota = forms.CharField(label="Mascota", required=False)
    edad_mascota = forms.IntegerField(label="Edad", required=False)
    sexo_mascota = forms.CharField(label="Sexo", required=False)
    raza_mascota = forms.CharField(label="Raza", required=False)
    nuevo_dueño = forms.CharField(label="Dueño", required=False)
    nueva_especie = forms.CharField(label="Especie", required=False)
    numero_ficha = forms.IntegerField(label="Número de Ficha")
    motivo_consulta = forms.CharField(label="Motivo de Consulta", required=False)

    class Meta:
        model = models.Ficha
        fields = ['numero_ficha', 'nueva_mascota', 'edad_mascota', 'sexo_mascota', 'raza_mascota', 'nuevo_dueño', 'nueva_especie', 'motivo_consulta']

    def save(self, commit=True):
        instance = super().save(commit=False)
        nueva_mascota_nombre = self.cleaned_data.get('nueva_mascota')
        edad_mascota = self.cleaned_data.get('edad_mascota')
        sexo_mascota = self.cleaned_data.get('sexo_mascota')
        raza_mascota = self.cleaned_data.get('raza_mascota')
        nuevo_dueño_nombre = self.cleaned_data.get('nuevo_dueño')
        nueva_especie_nombre = self.cleaned_data.get('nueva_especie')
        nuevo_motivo_consulta = self.cleaned_data.get('motivo_consulta')

        if nueva_mascota_nombre:
            nueva_mascota = models.Mascota.objects.create(
                nombre=nueva_mascota_nombre,
                edad=edad_mascota,
                sexo=sexo_mascota,
                raza=raza_mascota
            )
            instance.mascota = nueva_mascota
        elif instance.mascota:
            # Si no hay una nueva mascota, actualizamos la existente
            mascota = instance.mascota
            mascota.edad = edad_mascota if edad_mascota is not None else mascota.edad
            mascota.sexo = sexo_mascota if sexo_mascota is not None else mascota.sexo
            mascota.raza = raza_mascota if raza_mascota is not None else mascota.raza
            mascota.save()

        if nuevo_dueño_nombre:
            nuevo_dueño = models.Dueño.objects.create(nombre=nuevo_dueño_nombre)
            instance.dueño = nuevo_dueño

        if nueva_especie_nombre:
            nueva_especie = models.Especie.objects.create(nombre=nueva_especie_nombre)
            instance.especie = nueva_especie

        if nuevo_motivo_consulta:
            motivo_consulta = models.Consulta.objects.create(nombre=nuevo_motivo_consulta)
            instance.consulta = motivo_consulta

        if commit:
            instance.save()

        return instance