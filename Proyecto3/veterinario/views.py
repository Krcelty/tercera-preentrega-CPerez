from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .forms import CustomAuthenticationForm, CustomUserCreationForm


def index(request):
    return render(request, "veterinario/index.html")


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "veterinario/Login.html"

def register(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "Core/index.html", {"mensaje": f"Usuario '{username}' creado"})
    else:
        form = CustomUserCreationForm()
    return render(request, "veterinario/Registro.html", {"form": form})
