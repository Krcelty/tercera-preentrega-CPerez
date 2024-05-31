from django.urls import path
from tienda.views import index, IngresarMascotaCreate, FichaUpdateView,FichaListView,FichaDelete,FichaDetail


app_name = "tienda"

urlpatterns = [
     path("", index,name="index"),
     path("lista/list", FichaListView.as_view(), name="lista"),
     path("ingreso/create", IngresarMascotaCreate.as_view(),name="ingreso"),
     path('ficha_detail/detail/<int:pk>/', FichaDetail.as_view(), name='detalle'),
     path('modificacion/update/<int:pk>/', FichaUpdateView.as_view(), name='modificacion'),
     path('eliminar/delete/<int:pk>/', FichaDelete.as_view(), name='eliminar'),
   
 ]


