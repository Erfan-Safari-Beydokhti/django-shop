from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import request, JsonResponse
from django.template.loader import render_to_string
from django.views.generic import ListView, DeleteView, View

from .models import WishList


# Create your views here.

class WishListView(LoginRequiredMixin,ListView):
    model = WishList
    template_name = 'wishlist_module/wishlist.html'
    context_object_name = 'wishlists'
    def get_queryset(self):
        user=self.request.user
        return WishList.objects.filter(user=user).select_related('product').prefetch_related('product__category')
class WishDeleteItemView(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        wish=request.GET.get("wish_id")
        if not wish:
            return JsonResponse({"error":"no wish exists"}, status=400)

        try:
            item = WishList.objects.get(id=wish,user=request.user)
        except WishList.DoesNotExist:
            return JsonResponse({"error":"no wish exists"}, status=400)

        item.delete()
        wishlists=WishList.objects.filter(user=request.user).select_related('product').prefetch_related('product__category')
        html=render_to_string('wishlist_module/component/wishlist_items.html',{'wishlists':wishlists},request=request)
        return JsonResponse({"data":html})


