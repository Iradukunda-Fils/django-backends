<<<<<<< HEAD
# django-backends
=======
# Study Django Project

A Django-based web application with custom user authentication, profile management, and a secure dashboard.

## Features

- Custom user model with fields: email, bio, date of birth, profile picture, phone number, location
- PostgreSQL database support
- AJAX-powered login with real-time feedback
- User dashboard (only visible to authenticated users)
- Django admin integration for user management
- Responsive and modern UI with custom CSSfrom .views import logout_view

urlpatterns = [
    # ... other urls ...
    path('logout/', logout_view, name='logout'),
]

## Requirements

- Python 3.10+
- Django 5.x
- PostgreSQL
- Pillow
- psycopg2

## Setup Instructions

1. **Clone the repository**
    ```sh
    git clone <your-repo-url>
    cd study/django_project
    ```

2. **Create and activate a virtual environment**
    ```sh
    python -m venv .venv
    source .venv/bin/activate
    ```

3. **Install dependencies**
    ```sh
    pip install -r requirements.txt
    ```

4. **Install Pillow and psycopg2 if not in requirements**
    ```sh
    pip install Pillow psycopg2
    ```

5. **Configure your PostgreSQL database in `settings.py`**
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'back_ends_django_db',
            'USER': 'postgres',
            'PASSWORD': 'your_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

6. **Apply migrations**
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

7. **Create a superuser**
    ```sh
    python manage.py createsuperuser
    ```

8. **Run the development server**
    ```sh
    python manage.py runserver
    ```

9. **Access the app**
    - Visit [http://localhost:8000/](http://localhost:8000/)
    - Admin: [http://localhost:8000/admin/](http://localhost:8000/admin/)

## Project Structure

```
django_project/
├── account/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── login.html
│   │   └── dashboard.html
│   └── static/
│       └── css/
│           └── styles.css
├── django_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```

## Notes

- To use email for login, ensure your authentication backend supports it.
- Static and media files are configured in `settings.py`.
- For production, set `DEBUG = False` and configure `ALLOWED_HOSTS`.

---

**Author:** [Your Name]  
**License:** MIT
>>>>>>> eb28d60 (added data)
