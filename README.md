# Django Student Attachment Task

A Django REST Framework project for managing student attachments and data.

## Prerequisites

Before getting started, ensure you have the following installed on your system:

- **Python** 3.9 or higher
- **PostgreSQL** (database server) - must be installed and running
- **Pipenv** (for dependency management)

## Installation & Setup

### 1. Clone or Extract the Project

```bash
cd attachment_task
```

### 2. Activate Virtual Environment

```bash
pipenv shell
```

This installs all required dependencies from the `Pipfile` and activates the virtual environment.

### 3. Set Environment Variables (PostgreSQL Credentials)

Create a `.env` file in the project root directory and add your PostgreSQL credentials:

```env
SECRET_KEY=django-insecure-tbjfs-e_iclk#t+rvt=43rwu_%d#h-6!z7g7j_h7q@iu_)t90*
DEBUG=True
DB_NAME=student_db
DB_USER=postgres
DB_PASSWORD=your_postgres_password
DB_HOST=localhost
DB_PORT=5432
```

**Note:** Replace `your_postgres_password` with your actual PostgreSQL password.

### 4. Create PostgreSQL Database

Open PostgreSQL terminal (psql) or use a tool like pgAdmin, then run:

```sql
CREATE DATABASE student_db;
```

Or via command line:

```bash
createdb student_db
```

### 5. Run Database Migrations

```bash
python manage.py migrate
```

This creates all necessary tables in your PostgreSQL database.

### 6. Create Superuser (Optional - for Admin Access)

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

## Running the Development Server

```bash
python manage.py runserver
```

The server will start at: **http://127.0.0.1:8000/**

### Access Points:

- **Home**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/ (if you created a superuser)
- **API**: http://127.0.0.1:8000/api/ (REST endpoints)
            http://127.0.0.1:8000/students/ ( Get all student DATA)
            http://127.0.0.1:8000/students/<int:pk> ( Get Specific Student DATA)
            http://127.0.0.1:8000/students/create ( Create new student data)
## Project Structure

```
attachment_task/
├── attachment_task/          # Project settings & configuration
│   ├── settings.py           # Django settings (uses environment variables)
│   ├── urls.py               # Main URL configuration
│   ├── wsgi.py               # WSGI configuration
│   └── asgi.py               # ASGI configuration
├── students/                 # Django app
│   ├── models.py             # Database models
│   ├── views.py              # API views
│   ├── serializers.py        # DRF serializers
│   ├── urls.py               # App-specific URLs
│   ├── admin.py              # Django admin configuration
│   ├── migrations/           # Database migrations
│   └── tests.py              # Tests
├── manage.py                 # Django management script
├── Pipfile                   # Dependency management
├── db.sqlite3                # (For local testing - not used with PostgreSQL)
└── README.md                 # This file
```

## Environment Variables Reference

| Variable | Description | Default |
|----------|-------------|---------|
| `SECRET_KEY` | Django secret key for security | Set in settings.py |
| `DEBUG` | Enable debug mode | True |
| `DB_NAME` | PostgreSQL database name | student_db |
| `DB_USER` | PostgreSQL username | postgres |
| `DB_PASSWORD` | PostgreSQL password | playback009 |
| `DB_HOST` | PostgreSQL host | localhost |
| `DB_PORT` | PostgreSQL port | 5432 |

## Useful Commands

```bash
# Create a new migration for model changes
python manage.py makemigrations

# Apply migrations to database
python manage.py migrate

# Create superuser for admin access
python manage.py createsuperuser

# Run Django shell
python manage.py shell

# Collect static files (for production)
python manage.py collectstatic

# Exit virtual environment
exit
```

## Troubleshooting

### PostgreSQL Connection Error

**Error:** `psycopg2: connection refused`

**Solution:** 
- Ensure PostgreSQL is running on your system
- Check that your database credentials in `.env` are correct
- Verify the database exists: `createdb student_db`

### ModuleNotFoundError

**Error:** Missing dependencies

**Solution:** 
- Ensure you've run `pipenv shell` in the project root
- Run `pipenv install` to install all dependencies

### Database Already Exists

**Error:** `database "student_db" already exists`

**Solution:** Drop the existing database first:
```sql
DROP DATABASE student_db;
CREATE DATABASE student_db;
```

Then run migrations again.

## Notes for Submission

- Recipients should create their own `.env` file with their PostgreSQL credentials
- The `Pipfile` ensures all dependencies install correctly
- PostgreSQL must be pre-installed on the recipient's machine

## Support

For issues or questions, refer to:
- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
