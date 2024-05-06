from django.contrib import admin
from .models import Client, Product, Order


# Register your models here.


class ClientAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "phone", "address", "registration_date"]
    list_filter = ["name"]
    search_fields = ["name", "email", "phone"]
    list_per_page = 3

admin.site.register(Client, ClientAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price", "quantity"]
    list_filter = ["id"]
    search_fields = ["name"]
    list_per_page = 3

admin.site.register(Product, ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "client_name",
        "client_email",
        "client_phone",
        "client_address",
        "order_date",
        "product_list",
        "total_price",
        "status"
    ]
    list_filter = ["order_date",]
    search_fields = ["client__name",]
    list_per_page = 3
    actions = ["completed","incompleted"]

    # def client_id(self, obj):
    #     return obj.client.id

    def client_name(self, obj):
        return obj.client.name

    def client_email(self, obj):
        return obj.client.email

    def client_phone(self, obj):
        return obj.client.phone

    def client_address(self, obj):
        return obj.client.address

    def product_list(self, obj):
        return ', '.join([p.name for p in obj.products.all()])

    def completed(self, request, queryset):
        queryset.update(status=True)

    def incompleted(self, request, queryset):
        queryset.update(status=False)

admin.site.register(Order, OrderAdmin)
