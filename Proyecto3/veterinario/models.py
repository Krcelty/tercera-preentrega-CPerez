from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class veterinarioperfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="veterinarioperfil")
    celular = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to="avatares", null=True, blank=True)

    def __str__(self) -> str:
        return self.usuario.username
