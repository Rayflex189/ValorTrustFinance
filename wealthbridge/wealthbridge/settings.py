"""
Django settings for wealthbridge project.
"""

from pathlib import Path
import os
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# ==============================================================================
# CLOUDINARY CONFIGURATION
# ==============================================================================
cloudinary.config(
    cloud_name="dlzn0moho",
    api_key="563396395915366",
    api_secret="pCSSrLNvxfFSEzY4ZnaOiF5u93o"
)

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dlzn0moho',
    'API_KEY': '563396395915366',
    'API_SECRET': 'pCSSrLNvxfFSEzY4ZnaOiF5u93o',
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
MEDIA_URL = '/media/'

# ==============================================================================
# SECURITY CONFIGURATION
# ==============================================================================
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-default-dev-key-change-this')
DEBUG = os.environ.get('DEBUG', 'True') == 'True'
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# ==============================================================================
# APPLICATION DEFINITION
# ==============================================================================
INSTALLED_APPS = [
    # Django core
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    
    # Third party apps
    'cloudinary',
    'cloudinary_storage',
    
    # Local apps
    'bank_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'wealthbridge.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'wealthbridge.wsgi.application'

# ==============================================================================
# DATABASE CONFIGURATION
# ==============================================================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ==============================================================================
# PASSWORD VALIDATION
# ==============================================================================
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# ==============================================================================
# INTERNATIONALIZATION
# ==============================================================================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ==============================================================================
# STATIC FILES CONFIGURATION
# ==============================================================================
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static'] if (BASE_DIR / 'static').exists() else []
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ==============================================================================
# FLY.IO PRODUCTION SETTINGS
# ==============================================================================
FLY_APP_NAME = os.environ.get('FLY_APP_NAME', False)

if FLY_APP_NAME:
    # Database - Use persistent volume
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/app/data/db.sqlite3',
    }
    
    # Static files
    STATIC_ROOT = '/app/staticfiles'
    STATIC_URL = '/static/'
    
    # Security
    DEBUG = True
    ALLOWED_HOSTS = [
        'valortrustfinance.fly.dev',
        'valortrustfinance.it.com',
        'www.valortrustfinance.it.com',
        'localhost',
        '127.0.0.1',
    ]
    CSRF_TRUSTED_ORIGINS = [
        'https://valortrustfinance.fly.dev',
        'https://valortrustfinance.it.com',
        'https://www.valortrustfinance.it.com',
    ]
    
    # Secret key from environment
    SECRET_KEY = os.environ.get('SECRET_KEY', SECRET_KEY)
    
    # Ensure directories exist
    os.makedirs('/app/data', exist_ok=True)
    os.makedirs('/app/staticfiles', exist_ok=True)