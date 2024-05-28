from django.contrib import admin

from . import models

admin.site.register(models.Mascota)
admin.site.register(models.Dueño)
admin.site.register(models.Especie)
admin.site.register(models.Ficha )
admin.site.register(models.Consulta)


