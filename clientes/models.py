from django.db import models


class Cliente(models.Model):
    rut_empresa = models.CharField(max_length=12, unique=True)
    rubro = models.CharField(max_length=150)
    razon_social = models.CharField(max_length=200)
    telefono = models.CharField(max_length=30)
    direccion = models.CharField(max_length=255)
    contacto_nombre = models.CharField(max_length=150)
    contacto_email = models.EmailField()

    def __str__(self):
        return self.razon_social
