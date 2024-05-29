from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView
from tienda.models import Ficha
from .forms import MascotaForm


#se cambio la vista basada en funciones a vista basada en clases, como recomendo el profe
# def modificacion(request):
#     query = request.GET.get('q')
#     fichas = None
#     if query:
#         fichas = Ficha.objects.filter(mascota__nombre__icontains=query)
#     contexto = {"fichas": fichas}
#     return render(request, "tienda/modificacion.html", contexto)


class FichaMascotaUpdate(UpdateView):
    model = Ficha
    form_class = MascotaForm
    success_url = reverse_lazy("ficha_list")
    template_name = 'tienda/modificacion.html'



#se cambio la vista basada en funciones a vista basada en clases, como recomendo el profe
# def ingresar_mascota(request):
#     if request.method == 'POST':
#         form = MascotaForm(request.POST)
#         if form.is_valid():
#             mascota = form.save(commit=False)
#             mascota.numero_ficha = request.POST.get('numero_ficha')
#             mascota.save()
#             return redirect('tienda:index')  
#     else:
#         form = MascotaForm()
#     return render(request, 'tienda/ingreso.html', {'form': form})



#Vista basa en clases, para llenar mi form
class IngresarMascotaCreate(CreateView):
    model = Ficha
    form_class = MascotaForm
    success_url = reverse_lazy("tienda:index")
    template_name = 'tienda/ingreso.html'
    

def index(request):
    #fichas = Ficha.objects.all()
    return render(request, "tienda/index.html") #, {'fichas': fichas})


#Vista basa en clases, para ver todas las fichas listadas
class FichaListView(ListView):
    model = Ficha 
   
    def get_queryset(self) -> Any:
          queryset = super().get_queryset()
          return queryset