from decimal import Decimal, ROUND_HALF_UP

from django.core.validators import MinValueValidator
from django.db import models


class Producto(models.Model):
    sku = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=150)
    descripcion_corta = models.CharField(max_length=255)
    descripcion_larga = models.TextField()
    imagen = models.ImageField(upload_to="productos/")
    precio_neto = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(Decimal("0"))])
    precio_venta = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(Decimal("0"))])
    stock_actual = models.PositiveIntegerField()
    stock_minimo = models.PositiveIntegerField()
    stock_bajo = models.PositiveIntegerField()
    stock_alto = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        self.precio_venta = (self.precio_neto * Decimal("1.19")).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.sku} - {self.nombre}"
