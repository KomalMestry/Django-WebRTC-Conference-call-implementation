"""
WSGI config for conference_prj project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application
path = '/home/ubuntu/projects/conference_prj'   #path to project rckendoot
sys.path.append('/home/ubuntu/projects/conference_prj')
sys.path.append('/home/ubuntu/projects/conference_env/lib/python3.6/site-packages')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conference_prj.settings")

application = get_wsgi_application()
