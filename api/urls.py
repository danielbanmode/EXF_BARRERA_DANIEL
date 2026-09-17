from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ClienteViewSet, LoginAPIView, ProductoViewSet, UsuarioViewSet

router = DefaultRouter()
router.register("usuarios", UsuarioViewSet, basename="usuario")
router.register("productos", ProductoViewSet, basename="producto")
router.register("clientes", ClienteViewSet, basename="cliente")

urlpatterns = [
    path("login/", LoginAPIView.as_view(), name="api-login"),
    path("", include(router.urls)),
]
