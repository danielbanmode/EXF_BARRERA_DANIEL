from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import ProductoForm
from .models import Producto


@method_decorator(login_required, name="dispatch")
class ProductoListView(ListView):
    model = Producto
    template_name = "inventario/producto_list.html"
    context_object_name = "productos"


@method_decorator(login_required, name="dispatch")
class ProductoDetailView(DetailView):
    model = Producto
    template_name = "inventario/producto_detail.html"
    context_object_name = "producto"


@method_decorator(login_required, name="dispatch")
class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = "form.html"
    success_url = reverse_lazy("inventario:lista")


@method_decorator(login_required, name="dispatch")
class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = "form.html"
    success_url = reverse_lazy("inventario:lista")


@method_decorator(login_required, name="dispatch")
class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("inventario:lista")
