import datetime
from django.core.management.base import BaseCommand
from myapp2.models import Order

class Command(BaseCommand):
    help = "Create client."

    def handle(self, *args, **kwargs):
        order = Order ( products = 'Отвертка',total_price = '100',ordered_date = 10.04.2023)
        order.save()
        self.stdout.write(f"{order} {order.id} created.")
