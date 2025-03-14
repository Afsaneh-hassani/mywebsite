from mywebsite.settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-f8&_$fi+$oudui)6k7t34bsjg7sa6om+@rb%zxu9f6!m6dd!99'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []



#INSTALLED_APPS=[]

#site frameworks
SITE_ID=2


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

#X_FRAME_OPTION = 'SAVEORGIN'