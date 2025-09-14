from time import sleep
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    help = "Wait for database to be available"

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_conn = None
        attempts = 0
        while not db_conn:
            try:
                connections['default'].cursor()
                db_conn = True
            except OperationalError:
                attempts += 1
                self.stdout.write(f"DB not ready, retry {attempts}...")
                sleep(1)
        self.stdout.write(self.style.SUCCESS("Database available!"))
