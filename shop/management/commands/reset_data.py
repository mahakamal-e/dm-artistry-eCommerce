from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Delete all records from tables and reset sequences'

    def handle(self, *args, **kwargs):
        with connection.cursor() as cursor:
            # Disable foreign key checks
            cursor.execute('PRAGMA foreign_keys = OFF;')

            # Replace 'your_table_name' with your actual table names
            tables = ['shop_category', 'shop_product']  # Add your table names here
            for table in tables:
                # Delete all rows
                cursor.execute(f'DELETE FROM {table};')
                # Reset the sequence (AUTOINCREMENT) to 1
                cursor.execute(f'UPDATE sqlite_sequence SET seq = 0 WHERE name = "{table}";')
                self.stdout.write(self.style.SUCCESS(f'Table "{table}" cleared and sequence reset successfully'))

            # Re-enable foreign key checks
            cursor.execute('PRAGMA foreign_keys = ON;')
