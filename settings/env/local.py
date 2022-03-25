from settings.base import *  # noqa


# --------------------------------------------------------------
# DEBUG | WSGI
#
DEBUG = True
WSGI_APPLICATION = None

# --------------------------------------------------------------
# DATABASES | HOSTS
#
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),  # noqa
    }
}
ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
]
