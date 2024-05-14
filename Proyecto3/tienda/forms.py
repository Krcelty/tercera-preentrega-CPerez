from django import forms
from . import  models


class MascotaForm(forms.ModelForm):
    nueva_mascota = forms.CharField(label="Nueva Mascota", required=False)
    nuevo_dueño = forms.CharField(label="Nuevo Dueño", required=False)
    nueva_especie = forms.CharField(label="Nueva Especie", required=False)
    numero_ficha = forms.IntegerField(label="Número de Ficha")

    class Meta:
        model = models.Ficha
        fields = ['numero_ficha','nueva_mascota', 'nuevo_dueño', 'nueva_especie' ]

    def save(self, commit=True):
        instance = super().save(commit=False)
        nueva_mascota_nombre = self.cleaned_data.get('nueva_mascota')
        nuevo_dueño_nombre = self.cleaned_data.get('nuevo_dueño')
        nueva_especie_nombre = self.cleaned_data.get('nueva_especie')
        
        if nueva_mascota_nombre:
            nueva_mascota = models.Mascota.objects.create(nombre=nueva_mascota_nombre)
            instance.mascota = nueva_mascota
        
        if nuevo_dueño_nombre:
            nuevo_dueño =  models.Dueño.objects.create(nombre=nuevo_dueño_nombre)
            instance.dueño = nuevo_dueño
        
        if nueva_especie_nombre:
            nueva_especie =  models.Especie.objects.create(nombre=nueva_especie_nombre)
            instance.especie = nueva_especie
        return instance