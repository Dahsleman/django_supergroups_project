"""
WSGI config for new_telegram_bot_service project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'new_telegram_bot_service.settings'

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'new_telegram_bot_service.settings')

application = get_wsgi_application()
