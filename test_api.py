import json
import urllib.request
import urllib.error

BASE_URL = "http://localhost:8000/api/v1"

def run_tests():
    print("=== Iniciando Pruebas de API VentasFix ===")
    
    # 1. Login
    print("\n1. Probando Autenticación (POST /login/)...")
    login_data = json.dumps({
        "email": "admin@ventasfix.cl",
        "password": "admin"
    }).encode("utf-8")
    
    req = urllib.request.Request(f"{BASE_URL}/login/", data=login_data, headers={'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req) as response:
            res_data = json.loads(response.read().decode())
            token = res_data.get("token")
            print("✅ Login exitoso. Token obtenido.")
    except urllib.error.URLError as e:
        print("❌ Falla en Login:", e)
        return

    headers = {"Authorization": f"Token {token}"}

    # 2. Get Usuarios
    print("\n2. Probando Obtener Usuarios (GET /usuarios/)...")
    req = urllib.request.Request(f"{BASE_URL}/usuarios/", headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            print(f"✅ Usuarios obtenidos exitosamente. Cantidad: {len(data)}")
    except urllib.error.URLError as e:
        print("❌ Falla al obtener usuarios:", e)

    # 3. Get Productos
    print("\n3. Probando Obtener Productos (GET /productos/)...")
    req = urllib.request.Request(f"{BASE_URL}/productos/", headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            print(f"✅ Productos obtenidos exitosamente. Cantidad: {len(data)}")
    except urllib.error.URLError as e:
        print("❌ Falla al obtener productos:", e)

    # 4. Get Clientes
    print("\n4. Probando Obtener Clientes (GET /clientes/)...")
    req = urllib.request.Request(f"{BASE_URL}/clientes/", headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            print(f"✅ Clientes obtenidos exitosamente. Cantidad: {len(data)}")
    except urllib.error.URLError as e:
        print("❌ Falla al obtener clientes:", e)

    print("\n=== Pruebas Finalizadas ===")

if __name__ == "__main__":
    run_tests()
