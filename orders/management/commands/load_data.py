from django.core.management.base import BaseCommand
from orders.models import PaymentMethod

class Command(BaseCommand):
    help = 'Load initial data into the database'

    def handle(self, *args, **kwargs):
        payment_methods = [
            {'name': 'Cash on Delivery', 'description': 'Pay when you receive the order'},
            {'name': 'Credit Card', 'description': 'Pay using a credit card'},
        ]
        
        for method in payment_methods:
            PaymentMethod.objects.get_or_create(name=method['name'], defaults={'description': method['description']})
        
        self.stdout.write(self.style.SUCCESS('Successfully loaded initial data'))