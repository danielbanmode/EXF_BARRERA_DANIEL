from django.urls import path

from .views import (
    UsuarioCreateView,
    UsuarioDeleteView,
    UsuarioDetailView,
    UsuarioListView,
    UsuarioLoginView,
    UsuarioLogoutView,
    UsuarioUpdateView,
    dashboard,
)

app_name = "usuarios"

urlpatterns = [
    path("login/", UsuarioLoginView.as_view(), name="login"),
    path("logout/", UsuarioLogoutView.as_view(), name="logout"),
    path("dashboard/", dashboard, name="dashboard"),
    path("usuarios/", UsuarioListView.as_view(), name="lista"),
    path("usuarios/nuevo/", UsuarioCreateView.as_view(), name="crear"),
    path("usuarios/<int:pk>/", UsuarioDetailView.as_view(), name="detalle"),
    path("usuarios/<int:pk>/editar/", UsuarioUpdateView.as_view(), name="editar"),
    path("usuarios/<int:pk>/eliminar/", UsuarioDeleteView.as_view(), name="eliminar"),
]
