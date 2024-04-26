from django.core.management.base import BaseCommand
from myapp2.models import Client


class Command(BaseCommand):
    help = "Delete client by id."

    def add_arguments(self, parser):
        parser.add_argument("pk", type=int, help="Client ID")

    def handle(self, *args, **kwargs):
        pk = kwargs["pk"]
        user = Client.objects.filter(pk=pk).first()
        if user:
            user.delete()
            self.stdout.write(f"Client {pk} deleted.")
        else:
            self.stdout.write(f"Client {pk} not found.")
