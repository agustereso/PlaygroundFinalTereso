# PlaygroundFinalTereso – Blog de Viajes 🌍✈️

## 📝 Descripción

Este proyecto corresponde a la **Entrega Final – Playground Final Project (Coderhouse – Python/Django)**.

Es una aplicación web estilo **blog de viajes**, desarrollada con **Django**, que incluye:

- Manejo de usuarios (registro, login, logout).
- Perfiles de usuario con avatar y datos personales.
- CRUD completo de publicaciones de viajes.
- Editor de texto enriquecido para el contenido (CKEditor).
- Sistema de mensajería interna entre usuarios.
- Herencia de plantillas y navegación con Navbar.

---

## 🚀 Tecnologías utilizadas

- Python 3
- Django 4.x
- SQLite3 (como base de datos local)
- django-ckeditor (contenido enriquecido)
- HTML5 + Bootstrap 5
- Patrón **MVT (Model–View–Template)**

---

## 🧱 Estructura del proyecto

Aplicaciones principales del proyecto:

- **pages**

  - Modelo principal: `PostViaje`
  - Blog de viajes: listado, detalle, creación, edición y borrado de posts.

- **accounts**

  - Registro, login, logout.
  - Vista de perfil y edición de perfil.
  - Cambio de contraseña.
  - Modelo `Profile` asociado a `User` con:
    - avatar
    - bio
    - fecha de nacimiento
    - link

- **messaging**
  - Sistema de mensajería entre usuarios:
    - Bandeja de entrada
    - Mensajes enviados
    - Detalle de mensaje
    - Envío de nuevos mensajes

---

## 🗂️ Modelo principal: `PostViaje`

El modelo principal del blog de viajes cumple los requisitos de la consigna:

- `titulo` – `CharField`
- `destino` – `CharField`
- `contenido` – `RichTextField` (CKEditor)
- `imagen` – `ImageField`
- `fecha_publicacion` – `DateTimeField`
- `autor` – `ForeignKey` a `User`

Además, todas las apps se encuentran registradas en el panel de **admin de Django**.

---

## 🌐 Rutas principales

### Navegación general

| Sección           | URL                   | Descripción                        |
| ----------------- | --------------------- | ---------------------------------- |
| Home              | `/`                   | Página de inicio                   |
| About             | `/about/`             | Acerca de la autora / blog         |
| Listado de viajes | `/pages/`             | Listado de publicaciones de viajes |
| Detalle de viaje  | `/pages/<id>/`        | Detalle de una publicación         |
| Crear viaje       | `/pages/crear/`       | Crear nuevo post (requiere login)  |
| Editar viaje      | `/pages/<id>/editar/` | Editar post (requiere login)       |
| Borrar viaje      | `/pages/<id>/borrar/` | Borrar post (requiere login)       |

### Autenticación y perfiles

| Funcionalidad      | URL                          |
| ------------------ | ---------------------------- |
| Registro           | `/accounts/signup/`          |
| Login              | `/accounts/login/`           |
| Logout             | `/accounts/logout/`          |
| Ver perfil         | `/accounts/profile/`         |
| Editar perfil      | `/accounts/profile/edit/`    |
| Cambiar contraseña | `/accounts/password/change/` |

### Mensajería

| Funcionalidad      | URL                |
| ------------------ | ------------------ |
| Bandeja de entrada | `/mensajes/inbox/` |
| Mensajes enviados  | `/mensajes/sent/`  |
| Nuevo mensaje      | `/mensajes/new/`   |
| Detalle de mensaje | `/mensajes/<id>/`  |

---

## ▶️ Cómo ejecutar el proyecto en local

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/agustereso/PlaygroundFinalTereso.git
cd PlaygroundFinalTereso
```

2️⃣ Crear y activar entorno virtual  
python -m venv venv  
source venv/Scripts/activate

3️⃣ Instalar dependencias  
pip install -r requirements.txt

4️⃣ Aplicar migraciones  
python manage.py makemigrations  
python manage.py migrate

5️⃣ Crear superusuario (opcional pero recomendado)  
python manage.py createsuperuser

6️⃣ Ejecutar el servidor de desarrollo  
python manage.py runserver

Abrir en el navegador:  
http://127.0.0.1:8000/

📌 Flujo sugerido para probar la app:  
Ingresar a /accounts/signup/ y crear un usuario.  
Loguearse si es necesario desde /accounts/login/.  
Crear uno o más viajes desde /pages/crear/ o desde el admin.  
Navegar por el listado en /pages/ y entrar a los detalles.  
Editar y borrar un viaje (requiere estar logueado).  
Ir a /accounts/profile/ para ver y editar el perfil (avatar, bio, etc.).  
Probar el cambio de contraseña en /accounts/password/change/.  
Desde /mensajes/new/ enviar mensajes a otros usuarios.  
Ver la bandeja de entrada en /mensajes/inbox/ y enviados en /mensajes/sent/.
