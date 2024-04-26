from django.core.management.base import BaseCommand
from myapp2.models import Client


class Command(BaseCommand):
    help = "Create client."

    def handle(self, *args, **kwargs):
        client = Client(name='John',email='john@gmail.com',phone=+79999999999,address='Krasnodar',registration_date='20.04.2024')
        client.save()
        self.stdout.write(f"{client} {client.id} created.")
