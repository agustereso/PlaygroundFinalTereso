from pathlib import Path

# BASE DIR
BASE_DIR = Path(__file__).resolve().parent.parent


# ==========================
# SEGURIDAD
# ==========================
SECRET_KEY = "django-insecure-cambia-esto-si-queres"

DEBUG = True

ALLOWED_HOSTS = []


# ==========================
# APLICACIONES
# ==========================
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Terceros
    "ckeditor",

    # Apps propias
    "pages",
    "accounts",
    "messaging",
]


# ==========================
# MIDDLEWARE
# ==========================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# ==========================
# URLS / WSGI
# ==========================
ROOT_URLCONF = "PlaygroundFinalTereso.urls"

WSGI_APPLICATION = "PlaygroundFinalTereso.wsgi.application"


# ==========================
# TEMPLATES
# ==========================
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],  # usamos templates por app
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# ==========================
# BASE DE DATOS
# ==========================
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# ==========================
# PASSWORD VALIDATORS
# ==========================
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# ==========================
# INTERNACIONALIZACIÓN (ESPAÑOL)
# ==========================
LANGUAGE_CODE = "es-ar"

TIME_ZONE = "America/Argentina/Buenos_Aires"

USE_I18N = True
USE_TZ = True


# ==========================
# STATIC FILES
# ==========================
STATIC_URL = "/static/"


# ==========================
# MEDIA (IMÁGENES)
# ==========================
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


# ==========================
# AUTH (LOGIN / LOGOUT)
# ==========================
LOGIN_URL = "/accounts/login/"
LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "home"


# ==========================
# MENSAJES
# ==========================
from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.DEBUG: "secondary",
    messages.INFO: "info",
    messages.SUCCESS: "success",
    messages.WARNING: "warning",
    messages.ERROR: "danger",
}


# ==========================
# CKEDITOR
# ==========================
CKEDITOR_CONFIGS = {
    "default": {
        "toolbar": "full",
        "height": 300,
        "width": "100%",
    }
}


# ==========================
# DEFAULT FIELD
# ==========================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
