from celery import shared_task
from.models import Product
from django.db import transaction
from django.core.management import call_command
import json
import os


file_path='/home/niceiyke/Documents/WORK_FOLDER/product-discount-finder/priceFinder/output'

@shared_task
def loadproducts():
    call_command('loadProducts',)

@shared_task
def  remover_no_stock_products():
     call_command('deleteNoStockProducts',)


