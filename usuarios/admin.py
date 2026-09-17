from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ("email", "rut", "nombre", "apellido", "is_staff")
    ordering = ("email",)
    fieldsets = (
        (None, {"fields": ("email", "password")} ),
        ("Datos personales", {"fields": ("rut", "nombre", "apellido")} ),
        ("Permisos", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")} ),
    )
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "rut", "nombre", "apellido", "password1", "password2")} ),
    )
    search_fields = ("email", "rut", "nombre", "apellido")
