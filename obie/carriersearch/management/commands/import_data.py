from django.core.management.base import BaseCommand

from ._import_data import *


class Command(BaseCommand):
    
    help = "Data download from CSV"

    def handle(self, *args, **options):
        main()
