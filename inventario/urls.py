from django.urls import path

from .views import (
    ProductoCreateView,
    ProductoDeleteView,
    ProductoDetailView,
    ProductoListView,
    ProductoUpdateView,
)

app_name = "inventario"

urlpatterns = [
    path("", ProductoListView.as_view(), name="lista"),
    path("nuevo/", ProductoCreateView.as_view(), name="crear"),
    path("<int:pk>/", ProductoDetailView.as_view(), name="detalle"),
    path("<int:pk>/editar/", ProductoUpdateView.as_view(), name="editar"),
    path("<int:pk>/eliminar/", ProductoDeleteView.as_view(), name="eliminar"),
]
