# Doctorapp

Doctorapp es un proyecto desarrollado como parte del curso de Django REST Framework en [Platzi](https://platzi.com). Este proyecto tiene como objetivo construir una API RESTful para gestionar un sistema médico que incluye funcionalidades para pacientes, médicos, citas y más.

## Tecnologías
El proyecto está construido con las siguientes herramientas y tecnologías:

- **Django**: Framework principal para el desarrollo del backend.
- **Django REST Framework (DRF)**: Extensión para crear APIs REST de manera sencilla y escalable.
- **PostgreSQL**: Base de datos relacional utilizada en el proyecto.
- **Python**: Lenguaje de programación base para Django.

## Requisitos previos
Antes de iniciar, asegúrate de tener instalado lo siguiente en tu sistema:

- Python 3.8+
- pip (gestor de paquetes de Python)
- PostgreSQL

Opcionalmente, puedes usar herramientas como Docker para simplificar el entorno de desarrollo.

## Instalación
1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/tu-usuario/doctorpp.git
   cd doctorpp
   ```

2. **Crea un entorno virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # En Windows: venv\Scripts\activate
   ```

3. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configura la base de datos:**
   - Asegúrate de tener PostgreSQL en funcionamiento.
   - Crea una base de datos llamada `doctorpp` y un usuario con permisos.
   - Actualiza las credenciales de la base de datos en el archivo `settings.py`.

5. **Aplica las migraciones:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Crea un superusuario:**
   ```bash
   python manage.py createsuperuser
   ```

7. **Inicia el servidor de desarrollo:**
   ```bash
   python manage.py runserver
   ```

8. **Accede al panel de administración:**
   Ve a `http://127.0.0.1:8000/admin/` y usa las credenciales del superusuario que acabas de crear.


## Endpoints principales
El proyecto utiliza Django REST Framework para exponer los siguientes endpoints:

- **Pacientes:**
  - `GET /api/patients/` - Lista todos los pacientes.
  - `POST /api/patients/` - Crea un nuevo paciente.

- **Médicos:**
  - `GET /api/doctors/` - Lista todos los médicos.
  - `POST /api/doctors/` - Crea un nuevo médico.

- **Citas:**
  - `GET /api/appointments/` - Lista todas las citas.
  - `POST /api/appointments/` - Crea una nueva cita.

Consulta la documentación generada por DRF para obtener más detalles.

## Recursos adicionales
- [Documentación oficial de Django](https://docs.djangoproject.com/)
- [Documentación oficial de Django REST Framework](https://www.django-rest-framework.org/)
- [Curso en Platzi](https://platzi.com)