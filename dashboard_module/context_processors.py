from order_module.models import Order
from product_module.models import WishList


def dashboard_sidebar_context(request):
    if not request.user.is_authenticated:
        return {}
    return {'wish_count':WishList.objects.filter(user=request.user).count(),'order_count':Order.objects.filter(user=request.user).count(),'cancel_count':Order.objects.filter(user=request.user,status='canceled').count()}