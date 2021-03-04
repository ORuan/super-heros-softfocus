from pathlib import Path
import os
#import django_heroku


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

# TOKEN 7c846ea8924e6f9fafc0b3967737623907e775be>
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG") == 'True'
print(DEBUG)
"""
"localhost",
    "127.0.0.1",
    "0.0.0.0",
    "super-heros-softfocus-git-dev-back.ruanpb.vercel.app",
    "super-heros-softfocus.vercel.app",
"""
ALLOWED_HOSTS = ['*']


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "accounts",
    "superheros",
    "combats",

    "corsheaders",
    "rest_framework",
    "rest_framework.authtoken",
    "django_filters",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
]

# SSL SETTINGS
if DEBUG:
    pass
else:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True

# CORS HEADERS
CORS_ORIGIN_WHITELIST = [
    'https://super-heros-softfocus.vercel.app',
    'https://localhost:8000',
    'https://localhost:3000',
]
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'UPDATE',
    'PUT',
    'POST',
]
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'origin',
    'dnt',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "database.db",
    }
}

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

LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# STATICS-MEDIA  CONFIGS
STATIC_URL = "/static/"
MEDIA_URL = "/media/"

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

STATICFILES_DIRS = [
    BASE_DIR / "static",
    "/var/www/static/",
]

# Django Rest Framework
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 10,
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/second',
        'user': '1000/second'
    },
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',

    )

}

# setting accounts how user model default
AUTH_USER_MODEL = "accounts.Account"

# HEROKU
# django_heroku.settings(locals())
