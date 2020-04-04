import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Django не запустится, если secret_key не указан
SECRET_KEY = 'b%j)nuayw6so+a*i0iuzw)(*ghx1&72(n&e-*6htwz0kl)(&r4'
DEBUG = True # если False, понадобилось бы указать массив ALLOWED_HOSTS

ROOT_URLCONF = 'helloworld.urls' # главный модуль конфигурации url
WSGI_APPLICATION = 'helloworld.wsgi.application'

