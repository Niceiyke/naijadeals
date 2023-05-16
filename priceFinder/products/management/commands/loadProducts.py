from django.core.management.base import BaseCommand, CommandParser
import json
import os
from django.db import transaction
from products.models import Product

file_path='/djangoapp/scrapy_data/'

class Command(BaseCommand):
    help = 'load products'

    def add_arguments(self, parser: CommandParser) -> None:
        return super().add_arguments(parser)

    def handle(self, *args, **options):
            for file in os.listdir(file_path):
                print(file)
                with open(os.path.join(file_path,file),'r',encoding="utf8") as data:
                    x=json.load(data)

                    for i in x:
                        with transaction.atomic():
                            print(i)
                            if 'original_price' in i.keys():
                                Product.objects.update_or_create(name=i['name'],discount_price=i['discount_price'],original_price=i['original_price'],image=i['image'],product_url=i['url'],discount_percent=i['discount_percent'],category=i['category'],stock=i['stock'])
                            else:
                                continue


                    print('done')
