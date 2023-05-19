from .base import *



ALLOWED_HOSTS = ['*']

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get('DB_NAME'),
        "USER": os.environ.get('DB_USER'),
        "PASSWORD": os.environ.get('DB_PASSWORD'),
        "HOST": os.environ.get('DB_HOST'),
        "PORT": os.environ.get('DB_PORT'),
    }
}

print('connected')


CELERY_BROKER_URL = "amqp://admin:admin@3.145.24.76:5672/"
CELERY_RESULT_BACKEND = "redis://3.145.24.76:6379"
CELERY_MAX_TASKS_PER_CHILD = 1
CELERY_BROOKER_POOL_LIMIT=None


CELERY_BEAT_SCHEDULE = {
    "scrape": {
        "task": "scraper.tasks.scrape",
        "schedule": crontab(minute="*/10"),
    },

}




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = '/staticfiles/'
STATICFILES_DIRS = [BASE_DIR / "static"]
