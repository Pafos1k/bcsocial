"""Local development settings. Google OAuth credentials are read from .env."""
import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")
SECRET_KEY = "local-development-only-bcsocial-prototype"
DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "[::1]"]
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "frontend.apps.FrontendConfig",
]
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    # Every page requires sign-in unless its view is marked @login_not_required.
    "django.contrib.auth.middleware.LoginRequiredMiddleware",
]
ROOT_URLCONF = "bcsocial.urls"
TEMPLATES = [{
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "DIRS": [],
    "APP_DIRS": True,
    "OPTIONS": {"context_processors": [
        "django.template.context_processors.request",
        "django.contrib.auth.context_processors.auth",
        "django.contrib.messages.context_processors.messages",
    ]},
}]
WSGI_APPLICATION = "bcsocial.wsgi.application"
ASGI_APPLICATION = "bcsocial.asgi.application"
DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": BASE_DIR / "db.sqlite3"}}
LANGUAGE_CODE = "en-us"
TIME_ZONE = "America/New_York"
USE_TZ = True
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Authentication: Google sign-in only, restricted to bc.edu accounts.
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]
LOGIN_URL = "landing"
LOGIN_REDIRECT_URL = "home"
ACCOUNT_LOGOUT_REDIRECT_URL = "landing"
ACCOUNT_LOGIN_METHODS = {"email"}
ACCOUNT_SIGNUP_FIELDS = ["email*"]
ACCOUNT_EMAIL_VERIFICATION = "none"  # Google has already verified the address.
SOCIALACCOUNT_ONLY = True  # No local passwords; Google is the only way in.
SOCIALACCOUNT_LOGIN_ON_GET = True
SOCIALACCOUNT_AUTO_SIGNUP = True
SOCIALACCOUNT_ADAPTER = "frontend.adapters.BCSocialAccountAdapter"
ALLOWED_EMAIL_DOMAIN = "bc.edu"
SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "APPS": [{
            "client_id": os.environ.get("GOOGLE_CLIENT_ID", ""),
            "secret": os.environ.get("GOOGLE_CLIENT_SECRET", ""),
        }],
        "SCOPE": ["profile", "email"],
        # hd only pre-filters Google's account picker; the adapter enforces the domain.
        "AUTH_PARAMS": {"hd": ALLOWED_EMAIL_DOMAIN, "prompt": "select_account"},
    }
}
