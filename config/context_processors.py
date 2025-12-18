from django.contrib import messages

from cart_module.models import CartItem, Cart
from product_module.models import ProductCategory


def header_categories(request):
    cart = Cart.objects.get(user=request.user)
    return {
        'categories':ProductCategory.objects.filter(is_active=True,is_delete=False,parent__isnull=True),
        'cart_items' : existitems(request, cart),
        'sub_total':float(cart.total_price())
    }
def existitems(request, cart):
    if cart.items.exists():
        return CartItem.objects.filter(cart=cart, cart__user=request.user)
    else:
        messages.error(request, 'No cart items')