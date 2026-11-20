# Josrel Enriquez Ombion — Portfolio

A Django portfolio for a BSCS student developer, student leader, and agricultural-technology innovator.

## Before publishing

Open `pages/portfolio_data.py` and replace the `email`, `github_url`, `github_label`, and optional `linkedin_url` placeholders. The same file contains the page copy, skills, projects, and achievements.

## Run locally on Windows

```powershell
cd myworld
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/`. Create an admin account with `python manage.py createsuperuser` if needed.

## Publish to GitHub

Create an empty GitHub repository in your browser first. From the folder that contains `myworld`, run:

```powershell
git add myworld
git commit -m "Personalize Josrel Ombion portfolio"
git remote set-url origin https://github.com/YOUR-GITHUB-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

Replace both placeholders. Sign in to GitHub or use a personal access token if requested.

## Deploy on PythonAnywhere using Bash and `git clone`

Replace every uppercase placeholder. In PythonAnywhere, open **Consoles** → **Bash** and run:

```bash
git clone https://github.com/YOUR-GITHUB-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY/myworld
python3.10 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
```

Generate a secret key:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

In the **Web** tab, add a new web app using **Manual configuration** and the same Python version. Set the virtualenv to:

```text
/home/YOUR-PA-USERNAME/YOUR-REPOSITORY/myworld/.venv
```

Replace the contents of the WSGI file with:

```python
import os
import sys

project_home = '/home/YOUR-PA-USERNAME/YOUR-REPOSITORY/myworld'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

os.environ['DJANGO_SECRET_KEY'] = 'PASTE-YOUR-GENERATED-SECRET-KEY-HERE'
os.environ['DJANGO_DEBUG'] = '0'
os.environ['DJANGO_ALLOWED_HOSTS'] = 'YOUR-PA-USERNAME.pythonanywhere.com'
os.environ['DJANGO_CSRF_TRUSTED_ORIGINS'] = 'https://YOUR-PA-USERNAME.pythonanywhere.com'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

Press **Reload** in the Web tab, then visit `https://YOUR-PA-USERNAME.pythonanywhere.com`.

For updates later:

```bash
cd ~/YOUR-REPOSITORY
git pull
cd myworld
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
```

Press **Reload** in PythonAnywhere after the update. Keep the production secret key out of GitHub.
