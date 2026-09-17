from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import Usuario


class UsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=False, label="Contraseña")

    class Meta:
        model = Usuario
        fields = ["rut", "nombre", "apellido", "email", "password", "is_active", "is_staff"]

    def save(self, commit=True):
        usuario = super().save(commit=False)
        password = self.cleaned_data.get("password")
        if password:
            usuario.set_password(password)
        if commit:
            usuario.save()
        return usuario


class UsuarioCreationForm(UsuarioForm):
    password = forms.CharField(widget=forms.PasswordInput, required=True, label="Contraseña")


class LoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email")
