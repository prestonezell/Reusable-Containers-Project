from django.core.management.base import BaseCommand
from collector_checker import check_collector

class Command(BaseCommand):
    help = 'Check the collector and move products back to available products if needed'

    def handle(self, *args, **options):
        check_collector()
        self.stdout.write(self.style.SUCCESS('Collector check completed.'))
