from django.db import models

class Mascota(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.nombre
    
class Dueño(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.nombre

class Especie(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.nombre

class Edad(models.Model):
    edad = models.IntegerField()

    def __int__(self) -> int:
        return self.edad

class Peso(models.Model):
    peso = models.DecimalField(max_digits=4, decimal_places=2)

class Veterinario(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.nombre

class ficha(models.Model):
    numero_ficha = models.PositiveIntegerField(unique=True)
    mascota = models.ForeignKey(Mascota, on_delete=models.SET_NULL, null=True, blank=True )
    dueño = models.ForeignKey(Dueño, on_delete=models.SET_NULL, null=True, blank=True )
    especie = models.ManyToManyField(Especie)
    veterinario = models.ManyToManyField(Veterinario)




   


