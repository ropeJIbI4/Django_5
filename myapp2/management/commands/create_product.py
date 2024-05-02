from django.core.management.base import BaseCommand
from django.utils import timezone
from myapp2.models import Product


class Command(BaseCommand):
    help = "Добавляет продукты в базу данных"

    def add_arguments(self, parser):
        parser.add_argument(
            "product_names",
            metavar="N",
            type=str,
            nargs="+",
            help="список названий продуктов для добавления",
        )

    def handle(self, *args, **options):
        product_names = options["product_names"]

        products = []
        for name in product_names:
            product = Product(name=name, description=f"Описание для {name}")
            product.save()
            products.append(product)

        self.stdout.write(
            self.style.SUCCESS(
                "Успешно добавлено %s продуктов в базу данных" % len(products)
            )
        )
