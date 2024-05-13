from django.contrib import admin

from . import models

admin.site.register(models.Mascota)
admin.site.register(models.Dueño)
admin.site.register(models.Tipo)
admin.site.register(models.Edad)
admin.site.register(models.Peso)
admin.site.register(models.ficha)
