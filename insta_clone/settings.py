from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Media Files Configuration
MEDIA_URL = '/media/'  # URL path for accessing uploaded media files
MEDIA_ROOT = BASE_DIR / 'media'  # Directory where media files are stored locally

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--(tlk4_q%_g1v6mq7^)7w$y(gawdf^9lrq5d5r^cpuqf18xwdb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # Set to False in production

ALLOWED_HOSTS = ['instaclone-70sa.onrender.com']  # Add your deployment domain in production

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social',  # Custom app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
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

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django_project_db_hf2w',
        'USER': 'josh',
        'PASSWORD': 'k4BPrIyj4FWtNFh3t1GQduXmUmaRS1RM',
        'HOST': 'oregon-postgres.render.com',
        'PORT': '5432',
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

# Static files settings
STATIC_URL = '/static/'  # URL for static files

# Add STATICFILES_DIRS for development mode
STATICFILES_DIRS = [BASE_DIR / "static"]  # Directory for development

# STATIC_ROOT for production (when running collectstatic)
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Collect static files here for deployment

# Media files (uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Redirect after logout
LOGOUT_REDIRECT_URL = '/'

LOGIN_REDIRECT_URL = '/'  # Redirects to the home page after successful login

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Use your email provider's SMTP server
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'jcroly1998@gmail.com'  # Replace with your email address
EMAIL_HOST_PASSWORD = 'lpce tzdf amis qptg'  # email's app-specific password (Insta)
DEFAULT_FROM_EMAIL = 'jcroly1998@gmail.com'  # Default 'from' address for sending emails


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



