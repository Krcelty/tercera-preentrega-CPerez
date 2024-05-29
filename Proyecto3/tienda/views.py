from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView
from tienda.models import Ficha
from .forms import MascotaForm


def index(request):
    return render(request, "tienda/index.html")


class FichaUpdateView(UpdateView):
    model = Ficha
    form_class = MascotaForm
    template_name = 'tienda/modificacion.html'
    success_url = reverse_lazy('tienda:lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        if query:
            context['object_list'] = Ficha.objects.filter(mascota__nombre__icontains=query)
        return context


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
    


#Vista basa en clases, para ver todas las fichas listadas
class FichaListView(ListView):
    model = Ficha
    template_name = 'tienda/ficha_list.html'
    context_object_name = 'fichas'
   
    # def get_queryset(self) -> Any:
    #       queryset = super().get_queryset()
    #       return queryset
    def get_queryset(self) -> Any:
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(mascota__nombre__icontains=query)
        return queryset    