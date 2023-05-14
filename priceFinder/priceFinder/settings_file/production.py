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


CELERY_BROKER_URL = "redis://3.145.24.76:6379"
CELERY_RESULT_BACKEND = "redis://3.145.24.76:6379"

CELERY_BEAT_SCHEDULE = {
    "scrape": {
        "task": "scraper.tasks.scrape",
        "schedule": crontab(minute="*/2"),
    },
    "loadproducts": {
        "task": "products.tasks.loadproducts",
        "schedule": crontab(minute="*/5"),
    },

    "deleteproducts": {
        "task": "products.tasks.remover_no_stock_products",
        "schedule": crontab(minute="*/7"),
    },
}



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT ='/var/wwww/naijadeals/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
