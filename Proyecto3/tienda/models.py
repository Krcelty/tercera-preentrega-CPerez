from django.db import models

class Mascota(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.nombre
    
class Dueño(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.nombre

class Tipo(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.nombre

class Edad(models.Model):
    edad = models.IntegerField()

    def __int__(self) -> int:
        return self.edad

class Peso(models.Model):
    peso = models.DecimalField(max_digits=4, decimal_places=2)

class ficha(models.Model):
    nombre = models.PositiveIntegerField(unique=True)
    mascota = models.ForeignKey(Mascota, on_delete=models.SET_NULL, null=True, blank=True )
    dueño = models.ForeignKey(Dueño, on_delete=models.SET_NULL, null=True, blank=True )
    tipo = models.ManyToManyField(Tipo)




   


