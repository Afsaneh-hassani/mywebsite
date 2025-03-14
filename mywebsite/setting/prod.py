from mywebsite.settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-f8&_$fi+$oudui)6k7t34bsjg7sa6om+@rb%zxu9f6!m6dd!99'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

#site frameworks
SITE_ID=2

#INSTALLED_APPS=[]

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


STATIC_ROOT= BASE_DIR/'static'

MEDIA_ROOT= BASE_DIR/'media'

STATICFILES_DIRS = [
    BASE_DIR / "statics",
]


SECURE_BROWSER_XSS_FILTER= True
CSRF_COOKIE_SECURE=True


X_FRAME_OPTIONS = 'SAMEORIGIN'
#X-Content-Type-Options
SECURE_CONTENT_TYPE_NOSNIFF = True
## Strict-Transport-Security
SECURE_HSTS_SECONDS = 15768000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

## that requests over HTTP are redirected to HTTPS. aslo can config in webserver
#SECURE_SSL_REDIRECT = True 

# for more security
CSRF_COOKIE_SECURE = True
CSRF_USE_SESSIONS = True
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = 'Strict'



#compressor
COMPRESS_ROOT= STATIC_ROOT
COMPRESS_ENABLED= True

STATICFILES_FINDERS=(
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
     'compressor.finders.CompressorFinder',
    
    
)