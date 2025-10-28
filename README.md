# medical-clinic-website

A Django-based website for a medical clinic. The project includes the files for each tab, project settings, templates, and static assets (CSS, JS, images). 

## Key features
- Basic Django project scaffolding (project folder, `manage.py`).
- `accounts` app with templates for login/signup, dashboards and appointment handling.
- Static assets under `static/` (CSS, JS, images) and HTML templates under `templates/` and `accounts/templates/`.

## Repository layout (top-level)

- `manage.py` — Django management script.
- `project/` — Django project package (contains `settings.py`, `urls.py`, `wsgi.py`, etc.).
- `accounts/` — Django application for user management and clinic flows (views, models, templates, urls).
- `templates/` — site-level templates (homepage, about, specialties pages).
- `static/` — static assets grouped in subfolders: `css/`, `js/`, `images/`.

Example important files inside `accounts/`:
- `accounts/models.py` — app models (patients, appointments or user extensions if present).
- `accounts/views.py` — view functions and class-based views used by the app.
- `accounts/templates/` — contains the files for the website

## Requirements

- Python 3.8+ (or the version you use for Django projects).
- Django 

## Quick setup (Windows PowerShell)

1. Create and activate a virtual environment (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies

- Install Django (replace with exact version you prefer):

```powershell
pip install django
```

3. Apply migrations and create a superuser:

```powershell
python manage.py migrate
python manage.py createsuperuser
```

4. Run the development server:

```powershell
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.


## Notes about templates and static files

- Templates live in `templates/` and `accounts/templates/`. Adjust `TEMPLATES` settings in `project/settings.py` if you change paths.
- Static files are in `static/`.
