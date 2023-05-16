from celery import shared_task
from.models import Product
from django.db import transaction
from django.core.management import call_command
import json
import os



@shared_task
def loadproducts():
    call_command('loadProducts',)

@shared_task
def  remover_no_stock_products():
     call_command('deleteNoStockProducts',)


