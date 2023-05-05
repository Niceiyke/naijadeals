from django.core.management.base import BaseCommand, CommandParser
import json
import os
from products.models import Product

file_path='c:/Users/oyomi01/Documents/GitHub/Work_Folder/product-discount-finder/jumia.json'







class Command(BaseCommand):
    help = 'load products'

    def add_arguments(self, parser: CommandParser) -> None:
        return super().add_arguments(parser)
    
    def handle(self, *args, **options):
            with open(file_path,'r',encoding="utf8") as data:
                x=json.load(data)

                for i in x:
                    Product.objects.create(name=i['name'],discount_price=i['discount_price'],original_price=i['original_price'],image=i['image'])
                    
                print('done')