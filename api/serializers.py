from django.contrib.auth import authenticate
from rest_framework import serializers

from clientes.models import Cliente
from inventario.models import Producto
from usuarios.models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, min_length=8)

    class Meta:
        model = Usuario
        fields = ["id", "rut", "nombre", "apellido", "email", "password", "is_active", "is_staff"]
        read_only_fields = ["id"]

    def validate_email(self, value):
        if not value.lower().endswith("@ventasfix.cl"):
            raise serializers.ValidationError("El email debe terminar en @ventasfix.cl")
        return value

    def create(self, validated_data):
        password = validated_data.pop("password")
        return Usuario.objects.create_user(password=password, **validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        for field, value in validated_data.items():
            setattr(instance, field, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = "__all__"
        read_only_fields = ["id", "precio_venta"]


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"
        read_only_fields = ["id"]


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = authenticate(email=attrs["email"], password=attrs["password"])
        if not user:
            raise serializers.ValidationError("Credenciales invalidas")
        attrs["user"] = user
        return attrs
