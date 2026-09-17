from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, reverse_lazy
from django.views.generic import RedirectView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", RedirectView.as_view(url=reverse_lazy("usuarios:dashboard")), name="home"),
    path("", include("usuarios.urls")),
    path("inventario/", include("inventario.urls")),
    path("clientes/", include("clientes.urls")),
    path("api/v1/", include("api.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="api-schema"), name="api-docs"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
