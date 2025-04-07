import os
from .base import BASE_DIR
from dotenv import load_dotenv
import dj_database_url

# Load environment variables from .env file
load_dotenv()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv(
    "SECRET_KEY",
    # Use a less predictable fallback key for development
    "django-insecure-fallback-key-for-dev-" "!ty!p%v12@gxek#9gz4=k-hc$z_&02-(rw0a",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", "True") == "True"

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# Use dj-database-url to parse the DATABASE_URL environment variable
# Default to a local SQLite database if DATABASE_URL is not set
DATABASES = {
    "default": dj_database_url.config(default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}")
}

# Add any development-specific settings here, like email backend
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
