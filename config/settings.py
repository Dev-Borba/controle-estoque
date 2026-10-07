import os
from pathlib import Path

import dj_database_url
from dotenv import load_dotenv


# Pasta principal do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Carrega as configurações do arquivo .env
load_dotenv(BASE_DIR / ".env")


# Configuração para desenvolvimento local
SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY",
    "django-insecure-chave-de-desenvolvimento-controle-estoque",
)

DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]


# Aplicações
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "estoque",
]


# Middlewares
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# Rotas
ROOT_URLCONF = "config.urls"


# Templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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


# Aplicação WSGI
WSGI_APPLICATION = "config.wsgi.application"


# Banco de dados
database_url = os.getenv("DATABASE_URL", "").strip()

if database_url:
    # Usa o PostgreSQL do Neon
    DATABASES = {
        "default": dj_database_url.parse(
            database_url,
            conn_max_age=0,
        )
    }

    # Exige uma conexão criptografada
    DATABASES["default"].setdefault("OPTIONS", {}).setdefault(
        "sslmode",
        "require",
    )

    # Compatibilidade com o pool de conexões do Neon
    DATABASES["default"]["DISABLE_SERVER_SIDE_CURSORS"] = True

else:
    # Usa SQLite quando DATABASE_URL não está definida
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }


# Validação de senhas
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "MinimumLengthValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "CommonPasswordValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "NumericPasswordValidator"
        ),
    },
]


# Idioma e horário
LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_TZ = True


# Arquivos estáticos
STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR / "staticfiles"


# Tipo padrão dos identificadores
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"