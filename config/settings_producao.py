from pathlib import Path
from .settings import *

DEBUG = False

ALLOWED_HOSTS = ["gborba.pythonanywhere.com"]

CSRF_TRUSTED_ORIGINS = [
    "https://gborba.pythonanywhere.com",
]

SECRET_KEY = (
    Path.home() / ".controle-estoque-secret-key"
).read_text(encoding="utf-8").strip()

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True