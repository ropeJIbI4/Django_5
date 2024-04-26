from django.core.management.base import BaseCommand
from myapp2.models import Client


class Command(BaseCommand):
    help = "Update client by id."

    def add_arguments(self, parser):
        parser.add_argument("pk", type=int, help="Client ID")
        parser.add_argument("name", type=str, help="New name")

    def handle(self, *args, **kwargs):
        pk = kwargs["pk"]
        name = kwargs["name"]
        client = Client.objects.filter(pk=pk).first()
        if client:
            client.name = name
            client.save()
            self.stdout.write(f"Client {pk} updated.")
        else:
            self.stdout.write(f"Client {pk} not found.")
