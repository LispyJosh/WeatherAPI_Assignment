from pathlib import Path
from decouple import config

# 📌 Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# 📌 Media Files Configuration (For Image Uploads)
MEDIA_URL = '/media/'  # URL path for accessing uploaded media files
MEDIA_ROOT = BASE_DIR / 'media'  # Directory where media files are stored locally

# 📌 SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='django-insecure--(tlk4_q%_g1v6mq7^)7w$y(gawdf^9lrq5d5r^cpuqf18xwdb')

# 📌 SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

# 📌 Allowed hosts for deployment
ALLOWED_HOSTS = [
    'localhost',        # Local development
    '127.0.0.1',        # Local development IP address
    'weatherapi-assignment-3.onrender.com' #render.com
]

# 📌 Load API key from .env
API_KEY = config('API_KEY', default='')

# 📌 Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social',        # Insta Clone app
    'weather_app',   # Weather API app
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

ROOT_URLCONF = 'insta_clone.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  
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

WSGI_APPLICATION = 'insta_clone.wsgi.application'

# 📌 DATABASE CONFIGURATION - Currently using SQLite (Change if needed)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'weather_app_api',  # Database name
        'USER': 'weather_app_api_user',  # Username
        'PASSWORD': 'KEuTrgaz6l4zXRa6SVhAJsrFqtwkeTsW',  # Password
        'HOST': 'dpg-cufvlu2j1k6c73fvdq8g-a.oregon-postgres.render.com',  # Hostname
        'PORT': '5432',  # Default PostgreSQL port
    }
}


# 📌 Password validation settings
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 📌 Internationalization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# 📌 Static files settings (For CSS, JS, Images)
STATIC_URL = '/static/'  
STATICFILES_DIRS = [BASE_DIR / "static"]  
STATIC_ROOT = BASE_DIR / 'staticfiles'  

# 📌 Media files (For uploaded content)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# 📌 Login & Logout redirects
LOGIN_URL = '/login/'  # URL pattern for your login page for people who are not logged in
LOGIN_REDIRECT_URL = '/weather/'  # Redirect logged-in users here for people who have already logged in
 

# 📌 Email settings (For Forgot Email, Password Reset)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='jcroly1998@gmail.com')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='jgej ehvm wwhd exbk')  
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# 📌 Default primary key type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
