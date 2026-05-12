"""Compatibility shim for legacy `config.urls` imports."""

from pathlib import Path
import sys


MY_SITE_ROOT = Path(__file__).resolve().parent.parent / "my_site"

if str(MY_SITE_ROOT) not in sys.path:
    sys.path.insert(0, str(MY_SITE_ROOT))

from my_site.urls import urlpatterns
