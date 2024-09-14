from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.core.management import call_command

class OrdersConfig(AppConfig):
    name = 'orders'

    def ready(self):
        post_migrate.connect(load_initial_data, sender=self)

def load_initial_data(sender, **kwargs):
    call_command('load_data')