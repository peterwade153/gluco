"""
WSGI config for app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from utils.read_envs import read_env_file

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
if 'ENV_VAR_FILE' in os.environ:
    file_name = os.getenv('ENV_VAR_FILE')
    read_env_file(file_name)

application = get_wsgi_application()
