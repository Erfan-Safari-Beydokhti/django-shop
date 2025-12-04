from datetime import timezone
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import TemplateView, UpdateView, CreateView, ListView
from account_module.models import User
from dashboard_module.forms import AddPhoneForm, EditProfileForm, AddressForm
from dashboard_module.models import AddressBook
from order_module.models import Order


# Create your views here.
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard_module/dashboard.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        user = self.request.user
        context["full_name"]=user.get_full_name()
        context["email"]=user.email
        context["recent_orders"]=Order.objects.filter(user=user).order_by('-created')[:5]
        return context


class AddressCreateView(LoginRequiredMixin, CreateView):
    model = AddressBook
    form_class = AddressForm
    template_name = 'dashboard_module/dash_address_add.html'
    success_url = reverse_lazy('dash-address-book')
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)




class AddressUpdateView(LoginRequiredMixin, UpdateView):
    model = AddressBook
    form_class = AddressForm
    template_name = 'dashboard_module/dash_address_edit.html'
    success_url = reverse_lazy('dash-address-book')

    def get_queryset(self, **kwargs):
        return AddressBook.objects.filter(user=self.request.user)


class AddressListView(LoginRequiredMixin, ListView):
    model = AddressBook
    template_name = 'dashboard_module/dash_address_book.html'
    context_object_name = 'addresses'
    def get_queryset(self):
        return AddressBook.objects.filter(user=self.request.user).order_by('-id')




def dash_address_make_default(request):
    return render(request, 'dashboard_module/dash_address_make_default.html')


def dash_cancellation(request):
    return render(request, 'dashboard_module/dash_cancellation.html')


class EditProfileView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'dashboard_module/dash_edit_profile.html'
    form_class = EditProfileForm
    success_url = reverse_lazy('dash-my-profile')

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, "Your profile has been updated.")
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)





# def dash_my_order(request):
#     return render(request, 'dashboard_module/dash_my_order.html')

def dash_payment_option(request):
    return render(request, 'dashboard_module/dash_payment_option.html')

class MyProfileView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard_module/dash_my_profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["full_name"] = user.get_full_name()
        context["email"] = user.email
        context["phone"] = getattr(user, "phone", 'Please enter your mobile')
        context["birthday"] = getattr(user, "birth_date", 'Please enter your Birthday')
        gen = user.gender
        context["gender"] = 'Male' if gen == 'M' else 'Female' if gen == 'F' else None

        return context


# def dash_track_order(request):
#     return render(request, 'dashboard_module/dash_track_order.html')


class AddPhoneView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'dashboard_module/add_phone_number.html'
    form_class = AddPhoneForm
    success_url = reverse_lazy("dash-my-profile")

    def get_object(self):
        return self.request.user

def filter_order(request,user_id):
    filter=request.GET.get('filter','last_5_orders')
    orders=Order.objects.filter(user_id=user_id).order_by("-created")
    if filter=="last_5_orders":
        orders=Order.objects.filter(user_id=user_id).order_by('-created')[:5]
    elif filter=="last_15_days":
        days=timezone.now()-timezone.timedelta(days=15)
        orders=Order.objects.filter(user_id=user_id,created__gte=days).order_by('-created')
    elif filter=="last_30_days":
        days = timezone.now() - timezone.timedelta(days=30)
        orders = Order.objects.filter(user_id=user_id, created__gte= days).order_by('-created')
    elif filter=="last_6_months":
        days = timezone.now() - timezone.timedelta(days=186)
        orders = Order.objects.filter(user_id=user_id, created__gte= days).order_by('-created')
    html = render_to_string("dashboard_module/components/order_list.html",{"orders":orders})
    return JsonResponse({"html":html})


def make_default_shipping(request,pk):
    address = get_object_or_404(AddressBook,pk=pk,user=request.user)
    AddressBook.objects.filter(user=request.user).update(is_default_shipping=False)
    address.is_default_shipping = True
    address.save()
    return redirect('dash_address-book')

