from django.core.management.base import BaseCommand, CommandParser
from products.models import Product









class Command(BaseCommand):
    help = 'delete all products'

    def add_arguments(self, parser: CommandParser) -> None:
        return super().add_arguments(parser)
    
    def handle(self, *args, **options):
        
        products =Product.objects.all()

        products.delete()
        
        print('done')