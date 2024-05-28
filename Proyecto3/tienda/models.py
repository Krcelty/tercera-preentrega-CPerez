from django.db import models

class Mascota(models.Model):
    nombre = models.CharField(max_length=255)
    edad = models.PositiveIntegerField(null=True, blank=True)
    sexo = models.CharField(max_length=10, null=True, blank=True)
    raza = models.CharField(max_length=255, null=True, blank=True)

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

class Consulta(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.nombre 
    

class Ficha(models.Model):
    numero_ficha = models.PositiveIntegerField(unique=True)
    mascota = models.ForeignKey(Mascota, on_delete=models.SET_NULL, null=True, blank=True)
    dueño = models.ForeignKey(Dueño, on_delete=models.SET_NULL, null=True, blank=True)
    especie = models.ForeignKey(Especie, on_delete=models.SET_NULL, null=True, blank=True)
    consulta = models.ForeignKey(Consulta, on_delete=models.SET_NULL, null=True, blank=True)

    def str(self) -> str:
        return f"Ficha {self.numero_ficha}"

    @property
    def nombre_mascota(self):
        return self.mascota.nombre if self.mascota else None

    @property
    def edad_mascota(self):
        return self.mascota.edad if self.mascota else None

    @property
    def sexo_mascota(self):
        return self.mascota.sexo if self.mascota else None

    @property
    def raza_mascota(self):
        return self.mascota.raza if self.mascota else None






   


