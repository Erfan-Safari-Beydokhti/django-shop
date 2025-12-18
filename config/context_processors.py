from django.db.models import Sum

from cart_module.models import Cart
from product_module.models import ProductCategory


def header_categories(request):
    categories = ProductCategory.objects.filter(
        is_active=True,
        is_delete=False,
        parent__isnull=True
    )

    if not request.user.is_authenticated:
        return {
            'categories': categories,
            'cart_items_count': 0,
            'sub_total': 0
        }

    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_items_count = cart.items.aggregate(
        total=Sum('quantity')
    )['total'] or 0

    return {
        'categories': categories,
        'items': cart.items.all(),
        'cart_items_count': cart_items_count,
        'sub_total': float(cart.total_price())
    }
