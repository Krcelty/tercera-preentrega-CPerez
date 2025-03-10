from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.index,name="index"),
    path("core/contacto", views.contacto,name="contacto"),
   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)