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

class Ficha(models.Model):
    numero_ficha = models.PositiveIntegerField(unique=True)
    mascota = models.ForeignKey(Mascota, on_delete=models.SET_NULL, null=True, blank=True )
    dueño = models.ForeignKey(Dueño, on_delete=models.SET_NULL, null=True, blank=True )
    especie = models.ForeignKey(Especie, on_delete=models.SET_NULL, null=True, blank=True )

    def __str__(self) -> str:
        return f"Ficha {self.numero_ficha}"
    




   


