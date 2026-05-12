# AGENTS.md

## Cursor Cloud specific instructions

This is a Django 6.0.3 personal blog application using Python 3.12+ and SQLite.

### Services

| Service | Command | Notes |
|---------|---------|-------|
| Django dev server | `python3 manage.py runserver 0.0.0.0:8000` | Main app; serves the blog list at `/`, post detail at `/post/<slug>/`, and admin at `/admin/` |

### Quick reference

- **Install deps:** `pip install -r requirements.txt`
- **Migrate:** `python3 manage.py migrate`
- **Run tests:** `pytest -v` (configured in `pytest.ini`, uses `config.settings`)
- **Dev server:** `python3 manage.py runserver 0.0.0.0:8000`

### Known caveats

- The `blog/admin.py` imports `PostAdmin` but never calls `admin.site.register(Post, PostAdmin)`, so the Post model does not appear in Django admin.
- The runtime entrypoint remains `config.settings`, but it is now a compatibility shim that imports canonical settings from `my_site.settings`; use root `manage.py` commands and avoid mixing nested `my_site/manage.py` commands.
- `pip install` goes to `~/.local/`; ensure `~/.local/bin` is on `PATH` for `pytest`, `django-admin`, etc.
