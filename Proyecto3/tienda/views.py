from django.shortcuts import render, redirect

from . import models 
from .forms import MascotaForm

def index(request):
    consulta = models.Ficha.objects.all()
    contexto = {"ficha": consulta}
    return render(request,"tienda/index.html", contexto )


def modificacion(request):
    consulta = models.Ficha.objects.all()
    contexto = {"ficha": consulta}
    return render(request,"tienda/modificacion.html", contexto )


def ingresar_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            mascota = form.save(commit=False)
            mascota.numero_ficha = request.POST.get('numero_ficha')
            mascota.save()
            return redirect('tienda:index')  
    else:
        form = MascotaForm()
    return render(request, 'tienda/ingreso.html', {'form': form})