from gc import get_objects

from django.shortcuts import render
from django.contrib.auth.views import login_required
from django.shortcuts import get_object_or_404

from cart_module.models import Cart
from product_module.models import Product


# Create your views here.

@login_required()
def add_to_cart(request, product_id):
    product=get_object_or_404(Product, id=product_id)
    cart,created = Cart.objects.get_or_create(user=request.user)
    cart_item,created = Cart.objects.get_or_create(product=product,cart=cart)

    if created:
        cart_item.quantity += 1
        cart_item.save()


