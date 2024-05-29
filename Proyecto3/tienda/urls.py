from django.urls import path
from tienda.views import index, IngresarMascotaCreate, FichaMascotaUpdate,FichaListView


app_name = "tienda"

urlpatterns = [
     path("", index,name="index"),
     path("ingreso/", IngresarMascotaCreate.as_view(),name="ingreso"),
     path('modificacion/', FichaMascotaUpdate.as_view(), name='modificacion'),
     path("lista/", FichaListView.as_view(), name="lista"),
   
 ]


# urlpatterns += [
#     path("lista/", FichaListView.as_view,name="lista"), 
   
# ]
