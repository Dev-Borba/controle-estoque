import os

from django.core.exceptions import ImproperlyConfigured

from .settings import *


DEBUG = False


# Chave secreta definida nas variáveis de ambiente
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "").strip()

if not SECRET_KEY:
    raise ImproperlyConfigured(
        "Configure a variável DJANGO_SECRET_KEY."
    )


# Exige PostgreSQL em produção
if DATABASES["default"]["ENGINE"] != "django.db.backends.postgresql":
    raise ImproperlyConfigured(
        "Configure DATABASE_URL com a conexão PostgreSQL do Neon."
    )


# Domínios permitidos
ALLOWED_HOSTS = []

for variable in (
    "VERCEL_URL",
    "VERCEL_BRANCH_URL",
    "VERCEL_PROJECT_PRODUCTION_URL",
):
    domain = os.getenv(variable, "").strip()

    if domain and domain not in ALLOWED_HOSTS:
        ALLOWED_HOSTS.append(domain)

# Permite cadastrar domínios adicionais
for domain in os.getenv("DJANGO_ALLOWED_HOSTS", "").split(","):
    domain = domain.strip()

    if domain and domain not in ALLOWED_HOSTS:
        ALLOWED_HOSTS.append(domain)


# Origens autorizadas para formulários
CSRF_TRUSTED_ORIGINS = [
    f"https://{domain}"
    for domain in ALLOWED_HOSTS
]


# Arquivos estáticos
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"


# HTTPS e cookies
SECURE_PROXY_SSL_HEADER = (
    "HTTP_X_FORWARDED_PROTO",
    "https",
)

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True