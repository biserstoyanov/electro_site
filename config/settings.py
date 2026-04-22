import environ
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()
environ.Env.read_env(BASE_DIR / ".env")

SECRET_KEY = env("SECRET_KEY",default="test")
DEBUG = env.bool("DEBUG", default=False)
ALLOWED_HOSTS = ["stanelectric.energy","www.stanelectric.energy","130.204.145.28","*"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    "listings",
    "pages",
    "services",
    "about",
    "products",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",  # <-- важно
                "django.contrib.messages.context_processors.messages",  # <-- важно
                "pages.context_processors.global_variables",
            ],
        },
    },
]

DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_URL = "/static/"
#STATIC_ROOT = BASE_DIR / "/opt/electro_site/staticfiles"
STATIC_ROOT = '/opt/electro_site/staticfiles'
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "/opt/electro_site/media"
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail.privateemail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'info@stanelectric.energy'
EMAIL_TO_USER = 'stanelektrik.office@gmail.com'
EMAIL_HOST_PASSWORD = ''
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
WSGI_APPLICATION = 'config.wsgi.application'
