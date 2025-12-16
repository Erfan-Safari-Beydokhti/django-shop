from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.views.generic import ListView, View
from django.contrib import messages

from .models import WishList


# Create your views here.

class WishListView(LoginRequiredMixin, ListView):
    model = WishList
    template_name = 'wishlist_module/wishlist.html'
    context_object_name = 'wishlists'

    def get_queryset(self):
        qs = wishlist_exist(self.request)
        if not qs.exists():
            messages.warning(self.request, 'Your wishlist is empty')
        return qs


class WishDeleteItemView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        wish_id = request.GET.get("wish_id")

        if not wish_id:
            messages.error(request, "Item not found")
            return self._render(request)

        try:
            WishList.objects.get(id=wish_id, user=request.user).delete()
        except WishList.DoesNotExist:
            messages.error(request, "Item not found")
            return self._render(request)


        return self._render(request)

    def _render(self, request):
        wishlists = wishlist_exist(request)
        html = render_to_string(
            'wishlist_module/component/wishlist_items.html',
            {'wishlists': wishlists},
            request=request
        )
        return JsonResponse({"data": html})


def clear_wishlist(request):
    wish_list = WishList.objects.filter(user=request.user)
    wish_list.delete()
    return redirect('wishlist')


def wishlist_exist(request):
    return WishList.objects.filter(
        user=request.user
    ).select_related('product').prefetch_related('product__category')
