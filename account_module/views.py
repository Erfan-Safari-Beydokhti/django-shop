from django.shortcuts import render, redirect
from django.views.generic import View

from account_module.forms import RegisterForm


# Create your views here.

class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {'form': register_form}
        return render(request, 'account_module/register.html', context)
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        return render(request, 'account_module/register.html', {'form': form})
