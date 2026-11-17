"""Ambiente de Desenvolvimento"""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-chave-didatica-apenas-para-aula-local'
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
INSTALLED_APPS = ["django.contrib.staticfiles", "alunos"]
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
]

ROOT_URLCONF = "config.urls"
TEMPLATES = [{
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "DIRS": [BASE_DIR / "Templates"],

    "APP_DIRS": True,
}]

DATABASES = {"default": {
    "ENGINE": "django.db.backends.sqlite3",
    "NAME": BASE_DIR / "db.sqlite3",
}}

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "Static"]
LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Araguaina"
USE_TZ = True
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"