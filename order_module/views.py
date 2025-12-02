from lib2to3.fixes.fix_input import context

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, TemplateView
from account_module.models import User
from order_module.models import Order


# Create your views here.

class OrderListView(LoginRequiredMixin, ListView):
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = self.get_object()

        context['sub_total'] = order.get_total_price()
        shipping_fee = 0
        context['shipping_fee'] = shipping_fee
        context['total'] = shipping_fee + context['sub_total']
        return context


class TrackOrderView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard_module/dash_track_order.html"

    def post(self, request, *args, **kwargs):
        tracking_code = request.POST.get("order-id")
        email = request.POST.get("track-email")

        try:
            user = User.objects.get(email=email)
            order = Order.objects.get(payment_tracking_code=tracking_code, user=user)
        except (User.DoesNotExist, Order.DoesNotExist):
            messages.error(request, "Order Not Found!")
            return redirect('track-order')
        return redirect('order-detail', order.id)
