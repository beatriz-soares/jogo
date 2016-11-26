# -*- coding: utf-8 -*-
"""
WSGI config for torre_de_hanoi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "torre_de_hanoi.settings")

application = get_wsgi_application()
# Roda o whitenoise junto com a aplicação para servir os arquivos estáticos
application = DjangoWhiteNoise(application)
