"""
Django settings for annfsu_backend project.

Generated by 'django-admin startproject' using Django 5.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os
import firebase_admin
from pathlib import Path
from datetime import timedelta
from firebase_admin import credentials

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-&7-%9gsex15^46v)-@v4u73gip1=8rz(qxx$nye*_p-(l&w9xe"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "versatileimagefield",
    "authentication",
    "members",
    "news",
    "blood_donors",
    "notification",
    "team"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "annfsu_backend.urls"

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

WSGI_APPLICATION = "annfsu_backend.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles_build", "static")

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# URL that serves the files in MEDIA_ROOT
MEDIA_URL = "/media/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "authentication.User"


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "EXCEPTION_HANDLER": "core.exception_handler.custom_exception_handler",
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=600),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "AUTH_HEADER_TYPES": ("Bearer",),
}

JAZZMIN_SETTINGS = {
    "site_title": "ANNFSU Jhapa",
    "site_header": "ANNFSU Jhapa",
    "site_brand": "ANNFSU",
    "site_logo": "logo.png",
    "welcome_sign": "Welcome to the ANNFSU Jhapa Administration Portal",
    "copyright": "© ANNFSU Jhapa",
    "search_model": "blood_donors.BloodDonor",
    "user_avatar": "profile_picture",
    "theme": "superhero",
    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"model": "blood_donors.BloodDonor"},
        {"model": "news.News"},
        {"model": "news.Songs"},
        {"model": "authentication.User"},
        {
            "name": "Developer: Nishant Sapkota",
            "url": "https://snishant.com.np",
            "new_window": True,
        },
    ],
    "icons": {
        "authentication.User": "fa-solid fa-user",
        "auth.Group": "fa fa-users",
        "authentication.BlacklistedToken": "fas fa-ban",
        "blood_donors.BloodDonor": "fas fa-tint",
        "news.Songs": "fas fa-music",
        "news.News": "fas fa-newspaper",
    },
    "hide_models": ["authentication.BlacklistedToken"],
    "order_with_respect_to": [
        "authentication",
        "blood_donors",
        "news",
        "blood_donors.BloodDonor",
        "news.News",
        "news.Songs",
    ],
    "use_google_fonts_cdn": True,
    "navigation_expanded": True,
    "changeform_format": "single",
    "changeform_format_overrides": {
        "blood_donors.BloodDonor": "horizontal_tabs",
        "news.News": "collapsible",
        "news.Songs": "collapsible",
    },
    "custom_css": "css/custom_admin.css",
    "custom_js": "js/custom_js.js",
}

JAZZMIN_UI_TWEAKS = {
    "theme": "superhero",
    "dark_mode_theme": "superhero",
}

FIREBASE_CREDENTIALS_FILE = "core/config/firebase/serviceAccountKey.json"

if not firebase_admin._apps:
    cred = credentials.Certificate(FIREBASE_CREDENTIALS_FILE)
    firebase_admin.initialize_app(cred)
