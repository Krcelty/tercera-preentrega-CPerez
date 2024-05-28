from django.shortcuts import render, redirect

from . import models 
from .forms import MascotaForm


def modificacion(request):
    query = request.GET.get('q')
    fichas = None
    if query:
        fichas = models.Ficha.objects.filter(mascota__nombre__icontains=query)
    contexto = {"fichas": fichas}
    return render(request, "tienda/modificacion.html", contexto)


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


def index(request):
    fichas = models.Ficha.objects.all()
    return render(request, "tienda/index.html", {'fichas': fichas})
    
