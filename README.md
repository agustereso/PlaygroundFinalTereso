# 🌍 Playground Viajes

Playground Viajes es una aplicación web desarrollada en **Python con Django**, pensada como un blog de viajes donde los usuarios pueden compartir experiencias, contar sus recorridos y comunicarse entre ellos.  
Este proyecto fue realizado como trabajo final del curso de Python.

---

## 👩‍💻 Sobre el proyecto

La idea de la aplicación es combinar dos cosas que me gustan mucho:  
viajar y programar.

El sitio funciona como un **diario de viajes**, en el que cada usuario puede crear publicaciones con texto, imágenes y detalles del destino. Además, cuenta con un sistema de usuarios, perfiles personalizados y mensajería interna.

El foco del proyecto estuvo puesto en aplicar buenas prácticas de Django, organizar correctamente el código y que la aplicación sea clara y fácil de usar.

---

## 🧭 Funcionalidades principales

### Navegación general
- Home
- Acerca de mí
- Viajes
- Login / Registro
- Perfil
- Mensajes
- Logout

### Viajes (modelo principal)
- Listado de viajes publicados
- Vista de detalle de cada viaje
- Crear nuevos viajes
- Editar viajes (solo usuarios logueados)
- Eliminar viajes (solo usuarios logueados)
- Mensaje informativo cuando no hay viajes cargados

Cada viaje incluye:
- Título
- Subtítulo
- Texto enriquecido (CKEditor)
- Imagen
- Fecha de creación
- Categoría y destino

---

## 👤 Usuarios y perfiles

- Registro de usuarios con:
  - Username
  - Email
  - Password
- Login y logout
- Perfil de usuario con:
  - Nombre
  - Apellido
  - Email
  - Avatar
  - Biografía u otra información personal
- Edición de perfil
- Cambio de contraseña desde el perfil

---

## 💬 Mensajería

La aplicación cuenta con una **app de mensajería interna** que permite que los usuarios se comuniquen entre sí.

Incluye:
- Bandeja de entrada
- Mensajes enviados
- Envío de mensajes
- Vista de detalle de cada mensaje

---

## 🛠️ Tecnologías utilizadas

- Python 3
- Django
- Bootstrap 5
- HTML y CSS
- SQLite (solo para desarrollo)
- CKEditor

---

## ▶️ Cómo ejecutar el proyecto

Para ejecutar el proyecto de manera local, seguí estos pasos:

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/agustereso/PlaygroundFinalTereso.git

2. **Ingresar a la carpeta del proyecto**

cd PlaygroundFinalTereso


3. **Crear un entorno virtual**

python -m venv venv


4. **Activar el entorno virtual**

- ***En Windows:***

venv\Scripts\activate


- ***En Linux / macOS:***

source venv/bin/activate


5. **Instalar las dependencias**

pip install -r requirements.txt


6. **Ejecutar las migraciones**

python manage.py migrate


7. **Crear un superusuario (para acceder al admin)**

python manage.py createsuperuser


8. **Levantar el servidor de desarrollo**

python manage.py runserver


9. **Abrir el navegador e ingresar a**

http://127.0.0.1:8000/

---

## 🎥 Video demostración

En el siguiente video se muestra el funcionamiento general de la aplicación, navegación y funcionalidades principales:

https://drive.google.com/drive/folders/1ML8KjF-5YGoMs5uLylmA4CCiIkOhze-y?usp=sharing
