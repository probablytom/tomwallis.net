"""
WSGI config for tw_net project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tw_net.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


# For heroku deployment as per https://devcenter.heroku.com/articles/django-assets
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
