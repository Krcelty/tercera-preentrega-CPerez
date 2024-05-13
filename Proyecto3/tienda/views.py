from django.shortcuts import render

from . import models

def index(request):
    consulta = models.ficha.objects.all()
    contexto = {"ficha": consulta}
    return render(request,"tienda/index.html", contexto )
