from product_module.models import WishList


def dashboard_sidebar_context(request):
    if not request.user.is_authenticated:
        return {}
    return {'wish_count':WishList.objects.filter(user=request.user).count()}