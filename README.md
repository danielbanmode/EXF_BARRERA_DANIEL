# VentasFix

Sistema web para la administración de usuarios, inventario y clientes de VentasFix. Está desarrollado con Django y cuenta con una API REST protegida para integraciones externas.

## Nota personal

Elegí Python con Django porque ya tenía experiencia previa trabajando con este framework y me resultaba más cómodo que utilizar un stack nuevo. Django facilita el desarrollo mediante herramientas como su ORM, el escape automático de contenido en las plantillas y la protección integrada contra ataques comunes como XSS y CSRF.

Además, Django se integra fácilmente con Docker, lo que permite configurar el entorno de desarrollo de forma sencilla y mantener separadas las dependencias de la aplicación y de la base de datos.

## Funcionalidades

- Autenticación para la interfaz web.
- Gestión de usuarios, productos y clientes mediante operaciones CRUD.
- Dashboard con totales de usuarios, productos y clientes.
- Cálculo del precio de venta con IVA del 19% para los productos.
- API REST con autenticación por token.
- Documentación interactiva de la API con Swagger.
- Entorno de desarrollo preparado con Docker Compose y PostgreSQL.

## Tecnologías

- Python 3.11+
- Django 5
- Django REST Framework
- drf-spectacular
- PostgreSQL 16
- Docker y Docker Compose

## Instalación con Docker

### Requisitos

- Docker Desktop instalado y en ejecución.
- Git instalado para clonar el repositorio.

### Ejecución

1. Clona el repositorio:

   ```bash
   git clone https://github.com/danielbanmode/EXF_BARRERA_DANIEL.git
   cd EXF_BARRERA_DANIEL
   ```

2. Construye y levanta los servicios:

   ```bash
   docker compose up --build
   ```

   El servicio web ejecuta las migraciones automáticamente antes de iniciar Django.

3. Abre la aplicación en [http://localhost:8000](http://localhost:8000).

### Crear un usuario administrador

Con los contenedores en ejecución, abre otra terminal y ejecuta:

```bash
docker compose exec web python manage.py createsuperuser
```

Después podrás acceder al panel de administración en [http://localhost:8000/admin/](http://localhost:8000/admin/).

## Rutas principales

| Ruta | Descripción |
| --- | --- |
| `/` | Dashboard principal |
| `/admin/` | Panel de administración de Django |
| `/usuarios/` | Gestión de usuarios |
| `/inventario/` | Gestión de productos |
| `/clientes/` | Gestión de clientes |
| `/api/docs/` | Documentación Swagger de la API |
| `/api/schema/` | Esquema OpenAPI |

## API REST

La API está disponible bajo el prefijo `/api/v1/` y requiere autenticación por token.

### Autenticación

Envía las credenciales al endpoint de login:

```http
POST /api/v1/login/
Content-Type: application/json

{
  "email": "usuario@ventasfix.cl",
  "password": "tu-contrasena"
}
```

Usa el token recibido en las siguientes peticiones:

```http
Authorization: Token <tu-token>
```

### Recursos disponibles

- `/api/v1/login/`
- `/api/v1/usuarios/`
- `/api/v1/productos/`
- `/api/v1/clientes/`

### Métodos y respuestas HTTP

Los recursos `usuarios`, `productos` y `clientes` utilizan las operaciones estándar de un `ModelViewSet`:

| Método | Ruta | Respuesta esperada | Descripción |
| --- | --- | --- | --- |
| `GET` | `/api/v1/productos/` | `200 OK` | Devuelve la lista de productos. |
| `GET` | `/api/v1/productos/<id>/` | `200 OK` | Devuelve un producto específico. |
| `POST` | `/api/v1/productos/` | `201 Created` | Crea un producto y devuelve el registro creado. |
| `PUT` | `/api/v1/productos/<id>/` | `200 OK` | Reemplaza todos los datos del producto. |
| `PATCH` | `/api/v1/productos/<id>/` | `200 OK` | Actualiza parcialmente un producto. |
| `DELETE` | `/api/v1/productos/<id>/` | `204 No Content` | Elimina el producto correctamente. |

Las mismas operaciones están disponibles para `/usuarios/` y `/clientes/`.

#### Respuestas exitosas

Una consulta de lista (`GET`) devuelve un arreglo JSON:

```json
[
   {
      "id": 1,
      "nombre": "Producto de ejemplo"
   }
]
```

Una creación o actualización devuelve el objeto guardado. Por ejemplo, una respuesta `201 Created` puede tener esta estructura:

```json
{
   "id": 1,
   "nombre": "Producto de ejemplo",
   "precio_venta": "1190.00"
}
```

El endpoint de login responde `200 OK` y devuelve el token:

```json
{
   "token": "<tu-token>"
}
```

Una eliminación exitosa responde `204 No Content` y no incluye contenido en el cuerpo de la respuesta.

#### Respuestas de error

| Código | Nombre | Cuándo ocurre |
| --- | --- | --- |
| `400` | `Bad Request` | Los datos enviados son inválidos o faltan campos obligatorios. |
| `401` | `Unauthorized` | No se envió un token válido en `Authorization`. |
| `403` | `Forbidden` | El usuario está autenticado, pero no tiene permiso para realizar la operación. |
| `404` | `Not Found` | El recurso solicitado no existe, por ejemplo, `/api/v1/productos/999/`. |
| `405` | `Method Not Allowed` | Se utilizó un método HTTP que la ruta no permite. |

Ejemplo de error de validación (`400 Bad Request`):

```json
{
   "email": [
      "El email debe terminar en @ventasfix.cl"
   ]
}
```

Ejemplo de acceso sin autenticación (`401 Unauthorized`):

```json
{
   "detail": "Authentication credentials were not provided."
}
```

Ejemplo de recurso inexistente (`404 Not Found`):

```json
{
   "detail": "Not found."
}
```

La documentación completa está disponible en [Swagger UI](http://localhost:8000/api/docs/) cuando el proyecto está en ejecución.

## Pruebas

Con la aplicación levantada y un usuario creado, ejecuta:

```bash
python test_api.py
```

El script comprueba el login y la consulta de usuarios, productos y clientes mediante la API.

## Estructura del proyecto

```text
config/       Configuración y URLs principales de Django
usuarios/     Usuarios, autenticación y dashboard
inventario/   Productos e inventario
clientes/     Clientes
api/          Serializadores, vistas y URLs de la API
templates/    Plantillas HTML
static/       Archivos CSS y recursos estáticos
Dockerfile    Imagen del servicio web
docker-compose.yml
              Servicios web y PostgreSQL
manage.py     Herramienta de administración de Django
test_api.py   Pruebas básicas de la API
```

## Desarrollo local sin Docker

También es posible instalar las dependencias manualmente:

```bash
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Este modo requiere una instancia de PostgreSQL configurada mediante las variables `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST` y `DB_PORT`.
