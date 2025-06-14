## Django Internship Assignment

This is a Django-based backend project built as part of an internship assignment. It showcases key backend development concepts including REST API development, authentication, Celery for background tasks, and Telegram Bot integration.


## Tech Needed

- **Python 3.10+**
- **Django 4+**
- **Django REST Framework (DRF)**
- **Token Authentication**
- **Celery + Redis**
- **Telegram Bot API**
- **SQLite3 (default database)**


## Project Structure (Note:only the Main files are listed)

internship_project/
├── backend/ 
│ ├── settings.py
│ ├── urls.py
│ └── celery.py
| |
├── core/ # Main Django app
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ ├── serializers.py
│ ├── tasks.py
│ ├── telegram_bot.py
│ └── tests/
│ ├── test_login.py
│ └── test_register.py
├── manage.py
├── requirements.txt
└── README.md


## Features Implemented

 Feature                             Description                                                                 

  Public API                        Accessible without authentication (`/api/public/`)                          
  Protected API                     Requires Token Authentication (`/api/protected/`)                           
  User Registration API             Creates new user and sends welcome email using Celery                       
  Token Authentication              Token-based login via `/api/login/`                                         
  Background Email Sending          Welcome email sent asynchronously using Celery + Redis                     
  Telegram Bot Integration          Handles `/start` command and stores Telegram username in DB                 
  .env Configuration                Environment variables for secure production-style setup                     


## API Endpoints

## Public API
http
GET /api/public/
No authentication required.

## Protected API
GET /api/protected/
Headers:
Authorization: Token <your-token>

## Login (Token Auth)

POST /api/login/
Body (JSON):
{
  "username": "your_username",
  "password": "your_password"
}

Returns:
{ "token": "your_token" }

## Register

POST /api/register/
Body (JSON):
{
  "username": "newuser",
  "email": "newuser@example.com",
  "password": "StrongPassword123"
}
- Triggers a welcome email via Celery.

## Telegram Bot

Send /start to your bot
Your username will be stored in the database


## Environment Variables

SECRET_KEY=your_django_secret_key
DEBUG=True
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
TELEGRAM_BOT_TOKEN=your_telegram_bot_token

## Setup Instructions

- Clone the repo

git clone https://github.com/yourusername/internship_project.git
cd internship_project

- Setup virtual environment

python -m venv env
Windows: env\Scripts\activate

- Install dependencies

pip install -r requirements.txt

- Configure .env

cp .env.example .env (# fill in your real values in .env)

- Apply migrations and create superuser

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

- Start Redis server (for Celery)

redis-server

- Run Celery worker

celery -A backend worker --loglevel=info

- Run the Django server

python manage.py runserver

- Run Telegram Bot

python core/telegram_bot.py

## Note

- No frontend implemented.
- Console email backend is used for development.
- This project runs locally only.