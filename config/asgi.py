"""Compatibility shim for legacy `config.asgi` imports."""

from pathlib import Path
import os
import sys


MY_SITE_ROOT = Path(__file__).resolve().parent.parent / "my_site"

if str(MY_SITE_ROOT) not in sys.path:
    sys.path.insert(0, str(MY_SITE_ROOT))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_site.settings")

from my_site.asgi import application
