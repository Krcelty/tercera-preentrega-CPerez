from django.contrib.auth.views import LogoutView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from veterinario.views import CustomLoginView, index, register



app_name = "veterinario"

urlpatterns = [
    path("", index, name="index"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(template_name="veterinario/logout.html"), name="logout"),
    path("registro/", register, name="registro"),
   
]

urlpatterns += staticfiles_urlpatterns()