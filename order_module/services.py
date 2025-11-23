from cart_module.models import Cart
from order_module.models import Order, OrderItem


def create_order_from_cart(cart: Cart, tracking_code=None):
    order = Order.objects.create(
        user=cart.user,
        status='paid',
        payment_tracking_code=tracking_code,
    )
    total = 0

    for item in cart.items.all():
        OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity,
                                 price_at_purchase=item.product.price)
        total += item.product.price * item.quantity

    order.total_price = total
    order.save()

    cart.items.all().delete()
    cart.save()
    return order
