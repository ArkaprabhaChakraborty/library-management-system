"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.contrib.auth.models import User
from django.core.wsgi import get_wsgi_application

from dotenv import load_dotenv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_wsgi_application()

load_dotenv()
create_default_user = os.getenv("DJANGO_DEFAULT_SUPERUSER")

if (create_default_user):
    username = os.getenv("DJANGO_DEFAULT_SUPERUSER_USERNAME")
    email = os.getenv("DJANGO_DEFAULT_SUPERUSER_EMAIL")
    password = os.getenv("DJANGO_DEFAULT_SUPERUSER_PASSWORD")
    users = User.objects.all()
    if not users:
        User.objects.create_superuser(
            username=username, 
            email=email, 
            password=password, 
            is_active=True, 
            is_staff=True)