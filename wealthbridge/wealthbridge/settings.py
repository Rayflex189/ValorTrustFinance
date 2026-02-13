"""
Django settings for wealthbridge project.
"""

from pathlib import Path
import os
import cloudinary
import cloudinary.uploader
import cloudinary.api

cloudinary.config(
    cloud_name="dlzn0moho",
        api_key="563396395915366",
            api_secret="pCSSrLNvxfFSEzY4ZnaOiF5u93o"
            )

            # Build paths inside the project like this: BASE_DIR / 'subdir'.
            BASE_DIR = Path(__file__).resolve().parent.parent

            # SECURITY WARNING: keep the secret key used in production secret!
            SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-default-dev-key-change-this')

            # SECURITY WARNING: don't run with debug turned on in production!
            DEBUG = os.environ.get('DEBUG', 'True') == 'True'

            ALLOWED_HOSTS = ['localhost', '127.0.0.1']

            # Application definition
            INSTALLED_APPS = [
                'django.contrib.admin',
                    'django.contrib.auth',
                        'django.contrib.contenttypes',
                            'django.contrib.sessions',
                                'django.contrib.messages',
                                    'django.contrib.staticfiles',
                                        # Your apps here
                                            'django.contrib.humanize',
                                                'bank_app',
                                                    'cloudinary',
                                                        'cloudinary_storage',
                                                         # or whatever your app is called
                                                         ]

                                                         MIDDLEWARE = [
                                                             'django.middleware.security.SecurityMiddleware',
                                                                 'django.contrib.sessions.middleware.SessionMiddleware',
                                                                     'django.middleware.common.CommonMiddleware',
                                                                         'django.middleware.csrf.CsrfViewMiddleware',
                                                                             'django.contrib.auth.middleware.AuthenticationMiddleware',
                                                                                 'django.contrib.messages.middleware.MessageMiddleware',
                                                                                     'django.middleware.clickjacking.XFrameOptionsMiddleware',

                                                                                     'whitenoise.middleware.WhiteNoiseMiddleware',
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

                                                                                                                                                                                                                             # Default database - SQLite for development
                                                                                                                                                                                                                             DATABASES = {
                                                                                                                                                                                                                                 'default': {
                                                                                                                                                                                                                                         'ENGINE': 'django.db.backends.sqlite3',
                                                                                                                                                                                                                                                 'NAME': BASE_DIR / 'db.sqlite3',
                                                                                                                                                                                                                                                     }
                                                                                                                                                                                                                                                     }

                                                                                                                                                                                                                                                     # Password validation
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

                                                                                                                                                                                                                                                                                                                     # Internationalization
                                                                                                                                                                                                                                                                                                                     LANGUAGE_CODE = 'en-us'
                                                                                                                                                                                                                                                                                                                     TIME_ZONE = 'UTC'
                                                                                                                                                                                                                                                                                                                     USE_I18N = True
                                                                                                                                                                                                                                                                                                                     USE_TZ = True

                                                                                                                                                                                                                                                                                                                     # Static files (CSS, JavaScript, Images)
                                                                                                                                                                                                                                                                                                                     STATIC_URL = '/static/'
                                                                                                                                                                                                                                                                                                                     STATICFILES_DIRS = [BASE_DIR / 'static'] if (BASE_DIR / 'static').exists() else []
                                                                                                                                                                                                                                                                                                                     STATIC_ROOT = BASE_DIR / 'staticfiles'

                                                                                                                                                                                                                                                                                                                     CLOUDINARY_STORAGE = {
                                                                                                                                                                                                                                                                                                                         'CLOUD_NAME': 'dlzn0moho',
                                                                                                                                                                                                                                                                                                                             'API_KEY': '563396395915366',
                                                                                                                                                                                                                                                                                                                                 'API_SECRET': 'pCSSrLNvxfFSEzY4ZnaOiF5u93o',
                                                                                                                                                                                                                                                                                                                                 }

                                                                                                                                                                                                                                                                                                                                 MEDIA_URL = '/media/'  # or any prefix you choose
                                                                                                                                                                                                                                                                                                                                 DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


                                                                                                                                                                                                                                                                                                                                 # Default primary key field type
                                                                                                                                                                                                                                                                                                                                 DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

                                                                                                                                                                                                                                                                                                                                 # -------- FLY.IO PRODUCTION SETTINGS --------
                                                                                                                                                                                                                                                                                                                                 # Detect if we're running on Fly.io
                                                                                                                                                                                                                                                                                                                                 FLY_APP_NAME = os.environ.get('FLY_APP_NAME', False)

                                                                                                                                                                                                                                                                                                                                 if FLY_APP_NAME:
                                                                                                                                                                                                                                                                                                                                     # Use persistent volume for SQLite database
                                                                                                                                                                                                                                                                                                                                         DATABASES['default'] = {
                                                                                                                                                                                                                                                                                                                                                 'ENGINE': 'django.db.backends.sqlite3',
                                                                                                                                                                                                                                                                                                                                                         'NAME': '/app/data/db.sqlite3',
                                                                                                                                                                                                                                                                                                                                                             }
                                                                                                                                                                                                                                                                                                                                                                 
                                                                                                                                                                                                                                                                                                                                                                     # Static files configuration
                                                                                                                                                                                                                                                                                                                                                                         STATIC_ROOT = '/app/staticfiles'
                                                                                                                                                                                                                                                                                                                                                                             STATIC_URL = '/static/'
                                                                                                                                                                                                                                                                                                                                                                                 
                                                                                                                                                                                                                                                                                                                                                                                     # Security settings
                                                                                                                                                                                                                                                                                                                                                                                         DEBUG = False
                                                                                                                                                                                                                                                                                                                                                                                             ALLOWED_HOSTS = ['valortrustfinance.fly.dev', 'localhost', '127.0.0.1']
                                                                                                                                                                                                                                                                                                                                                                                                 
                                                                                                                                                                                                                                                                                                                                                                                                     # CSRF settings
                                                                                                                                                                                                                                                                                                                                                                                                         CSRF_TRUSTED_ORIGINS = ['https://valortrustfinance.fly.dev']
                                                                                                                                                                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                                                                                                                                 # Security middleware - add whitenoise for static files
                                                                                                                                                                                                                                                                                                                                                                                                                     MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
                                                                                                                                                                                                                                                                                                                                                                                                                         STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
                                                                                                                                                                                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                                                                                                                                                 # Ensure directories exist
                                                                                                                                                                                                                                                                                                                                                                                                                                     os.makedirs('/app/data', exist_ok=True)
                                                                                                                                                                                                                                                                                                                                                                                                                                         os.makedirs('/app/staticfiles', exist_ok=True)
                                                                                                                                                                                                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                                                                                                                                                                 # Secret key from environment
                                                                                                                                                                                                                                                                                                                                                                                                                                                     SECRET_KEY = os.environ.get('SECRET_KEY', SECRET_KEY)







                                                                                                                                                                                                                                                                                                                                                                                                                                                     