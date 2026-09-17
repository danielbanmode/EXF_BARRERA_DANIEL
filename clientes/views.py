from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import ClienteForm
from .models import Cliente


@method_decorator(login_required, name="dispatch")
class ClienteListView(ListView):
    model = Cliente
    template_name = "clientes/cliente_list.html"
    context_object_name = "clientes"


@method_decorator(login_required, name="dispatch")
class ClienteDetailView(DetailView):
    model = Cliente
    template_name = "clientes/cliente_detail.html"
    context_object_name = "cliente"


@method_decorator(login_required, name="dispatch")
class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "form.html"
    success_url = reverse_lazy("clientes:lista")


@method_decorator(login_required, name="dispatch")
class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "form.html"
    success_url = reverse_lazy("clientes:lista")


@method_decorator(login_required, name="dispatch")
class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("clientes:lista")
