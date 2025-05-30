FROM python:3.11-slim
WORKDIR /code
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# === backend/config/settings.py ===
# [Shortened: Include security configs, JWT, CORS]
INSTALLED_APPS = [
    ...
    'rest_framework',
    'corsheaders',
    'core',
]
AUTH_USER_MODEL = 'core.User'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}
