from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Count
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from clientes.models import Cliente
from inventario.models import Producto

from .forms import LoginForm, UsuarioCreationForm, UsuarioForm
from .models import Usuario


class UsuarioLoginView(LoginView):
    template_name = "registration/login.html"
    authentication_form = LoginForm


class UsuarioLogoutView(LogoutView):
    pass


@login_required
def dashboard(request):
    context = {
        "total_usuarios": Usuario.objects.count(),
        "total_productos": Producto.objects.count(),
        "total_clientes": Cliente.objects.count(),
    }
    return render(request, "dashboard.html", context)


@method_decorator(login_required, name="dispatch")
class UsuarioListView(ListView):
    model = Usuario
    template_name = "usuarios/usuario_list.html"
    context_object_name = "usuarios"


@method_decorator(login_required, name="dispatch")
class UsuarioDetailView(DetailView):
    model = Usuario
    template_name = "usuarios/usuario_detail.html"
    context_object_name = "usuario"


@method_decorator(login_required, name="dispatch")
class UsuarioCreateView(CreateView):
    model = Usuario
    form_class = UsuarioCreationForm
    template_name = "form.html"
    success_url = reverse_lazy("usuarios:lista")


@method_decorator(login_required, name="dispatch")
class UsuarioUpdateView(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = "form.html"
    success_url = reverse_lazy("usuarios:lista")


@method_decorator(login_required, name="dispatch")
class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("usuarios:lista")
