from django.core.management.base import BaseCommand
from catalog.models import Product, Category
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Load test data from fixture'

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        call_command('loaddata', 'catalog.json')
        self.stdout.write(self.style.SUCCESS('Successfully loaded data from fixture'))
