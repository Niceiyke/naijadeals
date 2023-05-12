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


AWS_ACCESS_KEY_ID='AKIAZPO36HGBOBRCLXTK'
AWS_SECRET_ACCESS_KEY='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'
AWS_STORAGE_BUCKET_NAME='pricefinderstatcfiles'
AWS_DEFAULT_ACL=None

STORAGES = {"default": {"BACKEND": "storages.backends.s3boto3.S3Boto3Storage"}}
STORAGES = {"staticfiles": {"BACKEND": "storages.backends.s3boto3.S3StaticStorage"}}