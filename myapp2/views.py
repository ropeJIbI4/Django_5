from datetime import *
from django.shortcuts import render,redirect
from .models import Order
from .forms import ProductForm


def ordered_products(request):

    now = datetime.now()

    orders_7_days = Order.objects.filter(
        order_date__range=[now - timedelta(days=7), now]
    ).prefetch_related("products")

    orders_30_days = Order.objects.filter(
        order_date__range=[now - timedelta(days=30), now]
    ).prefetch_related("products")

    orders_365_days = Order.objects.filter(
        order_date__range=[now - timedelta(days=365), now]
    ).prefetch_related("products")

    context = {
        "orders_7_days": orders_7_days,
        "orders_30_days": orders_30_days,
        "orders_365_days": orders_365_days,
    }

    return render(request, "index.html", context)


def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = ProductForm()
    return render(request, "create_product.html", {"form": form})
