"""
WSGI config for recrystal project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys

sys.path.append('/opt/moose/miniconda/lib/python2.7/site-packages')
from django.core.wsgi import get_wsgi_application


# Add the app's directory to the PYTHONPATH
sys.path.append('/home/qixinbo/projects/recrystal')
sys.path.append('/home/qixinbo/projects/recrystal/recrystal')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "recrystal.settings")

application = get_wsgi_application()
