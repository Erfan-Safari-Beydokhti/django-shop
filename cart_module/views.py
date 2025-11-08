from django.contrib.auth.views import login_required
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render

from cart_module.models import Cart, CartItem
from product_module.models import Product


# Create your views here.

@login_required()
def add_to_cart(request, product_id):
    product=get_object_or_404(Product, id=product_id)
    cart,created = Cart.objects.get_or_create(user=request.user)
    cart_item,created = Cart.objects.get_or_create(product=product,cart=cart)

    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart_detail')
@login_required()
def cart_detail(request):
    cart,created = Cart.objects.get_or_create(user=request.user)
    return render(request,'cart_module/cart.html',{'cart':cart})

@login_required()
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id,cart__user=request.user)
    item.delete()
    return redirect('cart_detail')



