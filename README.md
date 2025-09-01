# Expense Tracker

A Django-based web application for tracking expenses, with user authentication, dashboard, and bulk data management features.

## Features

- User authentication (login, logout, password management) via Allauth
- Dashboard for managing expenses, categories, and uploads
- Bulk upload data via CSV
- Responsive UI using Bootstrap/CoreUI
- Admin interface for advanced management
- Static and media file handling
- Docker support for easy deployment
- **Custom email backend for transactional email via ZeptoMail**

## Project Structure

```
.
├── .env
├── .env.example
├── .gitignore
├── Dockerfile
├── README.md
├── requirements.txt
├── requirements_railway.txt
├── requirements_codespace.txt
└── src/
    ├── db.sqlite3
    ├── manage.py
    ├── arvmain/
    ├── commando/
    ├── helpers/
    │   └── zeptomail_backend.py
    ├── local-cdn/
    ├── products/
    ├── staticfiles/
    ├── templates/
    └── userupload/
```

## Custom Email Backend

Transactional emails (such as account verification and notifications) are sent using a custom backend that integrates with ZeptoMail.  
The backend is implemented in [`helpers.zeptomail_backend.ZeptoMailBackend`](src/helpers/zeptomail_backend.py) and configured via environment variables:

- `ZEPTOMAIL_API_URL`
- `ZEPTOMAIL_API_TOKEN`

This ensures reliable delivery of important emails.

## Setup

### Prerequisites

- Python 3.10+
- pip
- Docker (optional)

### Installation

1. **Clone the repository:**
    ```sh
    git clone <repo-url>
    cd <repo-directory>
    ```

2. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Set up environment variables:**
    - Copy `.env.example` to `.env` and fill in the required values.

4. **Apply migrations:**
    ```sh
    cd src
    python manage.py migrate
    ```

5. **Download Vendors file from dropbox**

    This requires my own dropbox access key (no public key)

    ```sh
    python manage.py vendor_download /expense-tracker/
    ```

6. **Create a superuser:**
    ```sh
    python manage.py createsuperuser
    ```

7. **Create a superuser:**
    ```sh
    python manage.py createsuperuser
    ```

8. **Run the development server:**
    ```sh
    python manage.py runserver
    ```

## Usage

- Access the app at [http://localhost:8000/](http://localhost:8000/)
- Log in with your credentials or as the superuser.
- Use the dashboard to manage expenses and uploads.

## Static & Media Files

- Static files are located in staticfiles for development and by using collectstatic, they will be collected in /local-cdn folder and served using whitenoise
- Place custom static assets in `src/staticfiles/`.
- Templates use `{% static %}` for asset loading.

## Deployment

- Ready for deployment on platforms like Railway or Codespaces.
- See `requirements_railway.txt` and `requirements_codespace.txt` for environment-specific dependencies.
- The `Dockerfile` automates build and deployment steps specifically for Railway.com

---

**Note:** This application is intended for internal use. For access, please contact the