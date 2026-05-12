"""Compatibility shim for legacy `config.settings` imports.

Canonical settings now live in `my_site/settings.py`.
"""

from pathlib import Path
import sys


MY_SITE_ROOT = Path(__file__).resolve().parent.parent / "my_site"

if str(MY_SITE_ROOT) not in sys.path:
    sys.path.insert(0, str(MY_SITE_ROOT))

from my_site.settings import *  # noqa: F401,F403
