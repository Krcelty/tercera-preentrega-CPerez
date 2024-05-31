from django.contrib import messages
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView
from tienda.models import Ficha
from .forms import MascotaForm
from django.db.models import Q


def index(request):
    return render(request, "tienda/ficha_list.html")


#Vista basada en clases, para modificar mis ngresos del form 
class FichaUpdateView(UpdateView):
    model = Ficha
    form_class = MascotaForm
    template_name = 'tienda/modificacion.html'

    def form_valid(self, form):
        messages.success(self.request, "La ficha se modificó correctamente.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('tienda:modificacion', kwargs={'pk': self.get_object().pk})
 

#Vista basada en clases, para llenar mi form
class IngresarMascotaCreate(CreateView):
    model = Ficha
    form_class = MascotaForm
    success_url = reverse_lazy("tienda:ingreso")
    template_name = 'tienda/ingreso.html'
    
    def form_valid(self, form):
        messages.success(self.request, "La mascota se ingresó correctamente.")
        return super().form_valid(form)
    


#Vista basada en clases, para ver todas las fichas listadas y buscar 
class FichaListView(ListView):
    model = Ficha
    
    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        busqueda = self.request.GET.get("busqueda")
        if busqueda:
            queryset = Ficha.objects.filter(
                Q(dueño__nombre__icontains=busqueda) | Q(mascota__nombre__icontains=busqueda) 
            )
        return queryset    

class FichaDelete(DeleteView):
    model = Ficha
    success_url = reverse_lazy('tienda:lista')



class FichaDetail(DetailView):
    model = Ficha



