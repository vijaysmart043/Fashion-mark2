"""
Django settings for luxury e-commerce project.
Target market: India. Languages: English, Telugu. Currency: INR (₹).
"""

import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from .env if present
load_dotenv(BASE_DIR / '.env')

# Quick-start development settings - unsuitable for production
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-dev-key-change-me')

DEBUG = os.getenv('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1,.vercel.app,.run.app').split(',')
if DEBUG:
    ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = [
    'http://localhost:3000',
    'http://127.0.0.1:3000',
    'http://localhost:8000',
    'http://127.0.0.1:8000',
    'https://*.run.app',
    'https://*.vercel.app',
]

# Dummy / Placeholder Service Ports (assign production/custom ports via .env later)
SERVICE_PORTS = {
    'APP_PORT': int(os.getenv('PORT', 3000)),
    'DJANGO_DEV_PORT': int(os.getenv('DJANGO_DEV_PORT', 8000)),
    'ADMIN_PORT': int(os.getenv('ADMIN_PORT', 8001)),
    'API_PORT': int(os.getenv('API_PORT', 8002)),
    'DB_PORT': int(os.getenv('DB_PORT', 5432)),
    'REDIS_PORT': int(os.getenv('REDIS_PORT', 6379)),
    'EMAIL_PORT': int(os.getenv('EMAIL_PORT', 587)),
    'PAYMENT_WEBHOOK_PORT': int(os.getenv('PAYMENT_WEBHOOK_PORT', 8081)),
    'COURIER_WEBHOOK_PORT': int(os.getenv('COURIER_WEBHOOK_PORT', 8082)),
    'WORKER_PORT': int(os.getenv('WORKER_PORT', 8083)),
}


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    
    # Custom apps
    'apps.accounts.apps.AccountsConfig',
    'apps.core.apps.CoreConfig',
    'apps.catalog.apps.CatalogConfig',
    'apps.jewellery.apps.JewelleryConfig',
    'apps.sarees.apps.SareesConfig',
    'apps.inventory.apps.InventoryConfig',
    'apps.pricing.apps.PricingConfig',
    'apps.cart.apps.CartConfig',
    'apps.checkout.apps.CheckoutConfig',
    'apps.orders.apps.OrdersConfig',
    'apps.payments.apps.PaymentsConfig',
    'apps.shipping.apps.ShippingConfig',
    'apps.promotions.apps.PromotionsConfig',
    'apps.reviews.apps.ReviewsConfig',
    'apps.wishlist.apps.WishlistConfig',
    'apps.notifications.apps.NotificationsConfig',
    'apps.dashboard.apps.DashboardConfig',
    'apps.reports.apps.ReportsConfig',
    'apps.cms.apps.CmsConfig',
    'apps.search.apps.SearchConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

if not DEBUG:
    MIDDLEWARE.append('django.middleware.clickjacking.XFrameOptionsMiddleware')

ROOT_URLCONF = 'config.urls'

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
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database configuration with dj-database-url (Neon PostgreSQL support)
DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL', f'sqlite:///{BASE_DIR / "db.sqlite3"}'),
        conn_max_age=600,
        ssl_require=True if 'neon.tech' in os.getenv('DATABASE_URL', '') else False
    )
}


# Custom User Model
AUTH_USER_MODEL = 'accounts.User'


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


# Internationalization (English & Telugu)
LANGUAGE_CODE = 'en'

LANGUAGES = [
    ('en', 'English'),
    ('te', 'Telugu (తెలుగు)'),
]

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files (Cloudinary or Local)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
