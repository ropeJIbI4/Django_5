from django.urls import path
from . import views

urlpatterns = [
    path("product/", views.ordered_products, name="ordered_products"),
    path("create_product/", views.create_product, name="create_product")
]
