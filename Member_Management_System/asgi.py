"""
ASGI config for Member_Management_System project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "Member_Management_System.settings",
)

application = get_asgi_application()