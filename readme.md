
---

# FastAPI JWT Authentication

Este es un proyecto que implementa autenticación con **JWT** en una API construida con **FastAPI**. El proyecto está configurado para ser ejecutado dentro de un contenedor **Docker** y también puede ser ejecutado en un entorno local utilizando un entorno virtual.

## Características

* Autenticación mediante JWT.
* Gestión de usuarios y autenticación en rutas protegidas.
* Contenedor Docker para facilitar el despliegue.
* Entorno de desarrollo con dependencias gestionadas por `pip`.

---

## Requisitos

* **Python 3.11+**
* **Docker** (si deseas usar Docker para ejecutar la aplicación)
* **Docker Compose** (si deseas gestionar múltiples contenedores)

---

## Instalación

### 1. Clona el repositorio

```bash
git clone https://github.com/tu-usuario/fastapi-jwt.git
cd fastapi-jwt
```

### 2. Crear un entorno virtual (opcional, pero recomendado)

#### En Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### En macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

Una vez que el entorno virtual esté activado, instala las dependencias necesarias:

```bash
pip install -r requirements.txt
```

Si estás utilizando **Docker**, no es necesario instalar dependencias manualmente, ya que el contenedor se encarga de ello.

---

## Uso

### 1. Ejecutar la aplicación en local

Para ejecutar la aplicación de FastAPI localmente, usa el siguiente comando:

```bash
uvicorn app.main:app --reload
```

Este comando iniciará el servidor en `http://127.0.0.1:8000` y podrás acceder a la documentación de la API en `http://127.0.0.1:8000/docs`.

### 2. Ejecutar con Docker

Para correr la aplicación dentro de un contenedor Docker, primero, asegúrate de tener **Docker** y **Docker Compose** instalados en tu máquina. Luego, ejecuta:

```bash
docker-compose up --build
```

Este comando descargará las imágenes necesarias y construirá el contenedor si no está construido previamente.

**Puertos:**

* La API estará disponible en `http://localhost:8000`.

### 3. Acceso a la documentación

La API proporciona automáticamente una documentación interactiva en formato Swagger:

* **Ruta de documentación**: `http://localhost:8000/docs`
* **Redirección a documentación alternativa**: `http://localhost:8000/redoc`

---

## Variables de entorno

El proyecto usa un archivo `.env` para almacenar las configuraciones sensibles, como las claves secretas de JWT y la configuración de la base de datos.

Aquí tienes un ejemplo de un archivo `.env` básico:

```
# Configuración de JWT
SECRET_KEY=mi_clave_secreta
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Configuración de la base de datos
DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/mi_base_de_datos
```

**Variables de entorno**:

* `SECRET_KEY`: La clave secreta utilizada para firmar los tokens JWT.
* `ALGORITHM`: El algoritmo que se utilizará para firmar los JWT (por defecto `HS256`).
* `ACCESS_TOKEN_EXPIRE_MINUTES`: Tiempo de expiración del token en minutos.
* `DATABASE_URL`: URL de conexión para la base de datos PostgreSQL (si aplica).

---

## Estructura del proyecto

```plaintext
.
├── app/
│   ├── core/
│   │   ├── config.py      # Configuraciones principales
│   │   ├── security.py    # Seguridad y generación de JWT
│   │   └── settings.py    # Configuraciones de entorno
│   ├── models/
│   │   ├── user.py        # Modelo de usuario
│   └── routes/
│       ├── auth.py        # Rutas de autenticación (login, registro)
│       ├── users.py       # Rutas relacionadas con los usuarios
│   └── main.py            # Archivo principal donde se inicia la app
├── Dockerfile             # Configuración para la imagen Docker
├── docker-compose.yml     # Configuración de Docker Compose
├── requirements.txt       # Lista de dependencias
├── .env                   # Archivo de configuración de variables de entorno
└── README.md              # Este archivo
```

---

## Dockerfile

El archivo `Dockerfile` es responsable de crear una imagen del proyecto y contener toda la configuración necesaria para ejecutar la aplicación FastAPI.

### Dockerfile ejemplo:

```dockerfile
# Usar la imagen oficial de Python 3.11
FROM python:3.11-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos del proyecto
COPY . /app

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto
EXPOSE 8000

# Comando para ejecutar la aplicación con Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
```

### docker-compose.yml ejemplo:

```yaml
version: '3.8'
services:
  fastapi:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    environment:
      - DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/mi_base_de_datos
      - SECRET_KEY=mi_clave_secreta
      - ALGORITHM=HS256
      - ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## Comandos útiles

* **Instalar dependencias**:

  ```bash
  pip install -r requirements.txt
  ```

* **Ejecutar en desarrollo con Uvicorn**:

  ```bash
  uvicorn app.main:app --reload
  ```

* **Ejecutar con Docker**:

  ```bash
  docker-compose up --build
  ```

* **Detener contenedores Docker**:

  ```bash
  docker-compose down
  ```

* **Reiniciar contenedores Docker**:

  ```bash
  docker-compose restart
  ```

---

## Contribuciones

Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1. Haz un fork de este repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadir nueva funcionalidad'`).
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un pull request explicando tus cambios.

---

## Licencia

Este proyecto está licenciado bajo la **MIT License**. Para más detalles, consulta el archivo `LICENSE`.

---

Este archivo README cubre la instalación, uso, y configuraciones más importantes para tu proyecto. ¡Espero que te sea útil!
