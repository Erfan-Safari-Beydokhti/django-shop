from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from account_module.models import User
from order_module.models import Order


# Create your views here.

class OrderListView(LoginRequiredMixin,ListView):
    model = Order
    context_object_name = 'orders'
    template_name = 'dashboard_module/dash_my_order.html'
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).prefetch_related("items__product").order_by('-created')


class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = "dashboard_module/dash_manage_order.html"
    context_object_name = "order"

    def get_object(self):
        return Order.objects.get(id=self.kwargs["id"], user=self.request.user)

class TrackOrderView(TemplateView):
    template_name = "dashboard_module/dash_track_order.html"

    def post(self, request, *args, **kwargs):
        order_id = request.POST.get("order-id")
        email = request.POST.get("track-email")

        try:
            user = User.objects.get(email__iexact=email)
            order = Order.objects.get(order_id=order_id, user=user)
        except:
            return render(request, self.template_name, {
                "error": "Order Not Found!"
            })

        return render(request, self.template_name, {
            "order": order
        })