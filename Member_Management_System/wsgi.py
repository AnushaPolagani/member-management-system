"""
WSGI config for Member_Management_System project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "Member_Management_System.settings",
)

application = get_wsgi_application()