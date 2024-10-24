from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    "teste.mkverse.mkgcriacoes.com.br"
]

INSTALLED_APPS += [
    "mod_wsgi.server",
]