# BusNet — CS50 Web Bus Network Lab

A Django web app for browsing and booking bus routes, built with user authentication.

## Features
- Browse all available routes with origin, destination, and duration
- User registration, login, and logout
- Book or unbook a seat on any route (login required)
- Route detail page shows all passengers
- Deployed on Render with PostgreSQL and WhiteNoise

## Live URL
<!-- Add your Render URL here -->

## Local Development

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
