from django.core.management.base import BaseCommand, CommandParser
from products.models import Product


class Command(BaseCommand):
    help = 'delete products with no stock'

    def add_arguments(self, parser: CommandParser) -> None:
        return super().add_arguments(parser)
    
    def handle(self, *args, **options):
        
        qs=Product.objects.filter(stock="Sold out")
        num_product=len(qs)
        qs.delete()
        print(f'{num_product} was deleted')