import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Django не запустится, если secret_key не указан
SECRET_KEY = 'b%j)nuayw6so+a*i0iuzw)(*ghx1&72(n&e-*6htwz0kl)(&r4'
DEBUG = True # если False, понадобилось бы указать массив ALLOWED_HOSTS

ROOT_URLCONF = 'core.urls' # главный модуль конфигурации url
WSGI_APPLICATION = 'core.wsgi.application'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
#MEDIA_ROOT = '/root/python_practice/dj/aboard/media/'

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'rest_framework',
    'user',
    'authentication',
    'catalog',
    'album',
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ]
}

'''
# просто раскомментировать и использовать redis
SESSION_ENGINE = 'redis_sessions.session'

SESSION_REDIS = {
    'host': '192.168.102.2',
    'port': 6379,
    'db': 0,
    'password': 'password',
    'prefix': 'session',
    'socket_timeout': 1
}
'''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dj_aboard',
        'HOST': 'localhost',
        'USER': 'test',
        'PASSWORD': 'test'
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
#        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
#                'django.template.context_processors.debug',
                'django.template.context_processors.request',
#                'django.contrib.auth.context_processors.auth',
#                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# celery
BROKER_URL = 'redis://guest:password@192.168.102.2:6379/0'
CELERY_RESULT_BACKEND = 'redis://guest:password@192.168.102.2:6379/0'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
