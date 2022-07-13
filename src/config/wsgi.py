"""
WSGI config for deniskrumko project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from whitenoise import WhiteNoise

from core.display import print_msg

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

application = WhiteNoise(get_wsgi_application())

# Display admin and frontend URLs
# ========================================================================

print_msg('\nWEB:\thttp://127.0.0.1:8000/', wrap=False)
print_msg('ADMIN:\thttp://127.0.0.1:8000/admin/\n', wrap=False)
