from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView
from account_module.models import User
from dashboard_module.forms import AddPhoneForm, EditProfileForm


# Create your views here.
def dashboard(request):
    return render(request,'dashboard_module/dashboard.html')
def dash_address_add(request):
    return render(request,'dashboard_module/dash_address_add.html')
def dash_address_edit(request):
    return render(request,'dashboard_module/dash_address_edit.html')
def dash_address_book(request):
    return render(request,'dashboard_module/dash_address_book.html')
def dash_address_make_default(request):
    return render(request,'dashboard_module/dash_address_make_default.html')
def dash_cancellation(request):
    return render(request,'dashboard_module/dash_cancellation.html')
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

def dash_manage_order(request):
    return render(request,'dashboard_module/dash_manage_order.html')
def dash_my_order(request):
    return render(request,'dashboard_module/dash_my_order.html')
class MyProfileView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard_module/dash_my_profile.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        user=self.request.user
        context["full_name"]=user.get_full_name()
        context["email"]=user.email
        context["phone"]=getattr(user,"phone",'Please enter your mobile')
        context["birthday"]=getattr(user,"birthday",'Please enter your Birthday')
        gen=user.gender
        context["gender"]= 'Male' if gen=='M' else 'Female' if gen=='F' else None

        return context


def dash_track_order(request):
    return render(request,'dashboard_module/dash_track_order.html')

class AddPhoneView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'dashboard_module/add_phone_number.html'
    form_class = AddPhoneForm
    success_url = reverse_lazy("dash-my-profile")
    def get_object(self):
        return self.request.user