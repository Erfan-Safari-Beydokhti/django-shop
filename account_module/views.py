import datetime

from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from django.views.generic import View

from account_module.forms import RegisterForm
from account_module.models import User


# Create your views here.

class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {'form': register_form}
        return render(request, 'account_module/register.html', context)

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            if User.objects.filter(email__iexact=email).exists():
                form.add_error('email', 'Email already registered.')
            else:
                new_user = User(email=email, username=email, active_email_code=get_random_string(48), is_active=False)
                new_user.set_password(password)
                new_user.first_name=form.cleaned_data['first_name']
                new_user.last_name=form.cleaned_data['last_name']
                y,m,d=int(form.cleaned_data['year']), int(form.cleaned_data['month']), int(form.cleaned_data['day'])
                new_user.birth_date=datetime.date(y,m,d)
                new_user.gender=form.cleaned_data['gender']
                new_user.save()


