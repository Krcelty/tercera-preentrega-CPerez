from django import forms
from . import models

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

    def __init__(self, *args, **kwargs):
        super(MascotaForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['nueva_mascota'].initial = self.instance.nombre_mascota
            self.fields['edad_mascota'].initial = self.instance.edad_mascota
            self.fields['sexo_mascota'].initial = self.instance.sexo_mascota
            self.fields['raza_mascota'].initial = self.instance.raza_mascota
            self.fields['nuevo_dueño'].initial = self.instance.dueño.nombre if self.instance.dueño else ''
            self.fields['nueva_especie'].initial = self.instance.especie.nombre if self.instance.especie else ''
            self.fields['motivo_consulta'].initial = self.instance.consulta.nombre if self.instance.consulta else ''

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
            if instance.mascota:
                mascota = instance.mascota
                mascota.nombre = nueva_mascota_nombre
                mascota.edad = edad_mascota
                mascota.sexo = sexo_mascota
                mascota.raza = raza_mascota
                mascota.save()
            else:
                nueva_mascota = models.Mascota.objects.create(
                    nombre=nueva_mascota_nombre,
                    edad=edad_mascota,
                    sexo=sexo_mascota,
                    raza=raza_mascota
                )
                instance.mascota = nueva_mascota
        elif instance.mascota:
            mascota = instance.mascota
            mascota.edad = edad_mascota if edad_mascota is not None else mascota.edad
            mascota.sexo = sexo_mascota if sexo_mascota is not None else mascota.sexo
            mascota.raza = raza_mascota if raza_mascota is not None else mascota.raza
            mascota.save()

        if nuevo_dueño_nombre:
            if instance.dueño:
                instance.dueño.nombre = nuevo_dueño_nombre
                instance.dueño.save()
            else:
                nuevo_dueño = models.Dueño.objects.create(nombre=nuevo_dueño_nombre)
                instance.dueño = nuevo_dueño

        if nueva_especie_nombre:
            if instance.especie:
                instance.especie.nombre = nueva_especie_nombre
                instance.especie.save()
            else:
                nueva_especie = models.Especie.objects.create(nombre=nueva_especie_nombre)
                instance.especie = nueva_especie

        if nuevo_motivo_consulta:
            if instance.consulta:
                instance.consulta.nombre = nuevo_motivo_consulta
                instance.consulta.save()
            else:
                motivo_consulta = models.Consulta.objects.create(nombre=nuevo_motivo_consulta)
                instance.consulta = motivo_consulta

        if commit:
            instance.save()

        return instance
