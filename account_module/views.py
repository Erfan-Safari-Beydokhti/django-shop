import datetime
from lib2to3.fixes.fix_input import context

from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.views.generic import View

from account_module.forms import RegisterForm, LoginForm
from account_module.models import User
from utils.email import send_email


import datetime
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.views import View

from account_module.forms import RegisterForm
from account_module.models import User
from utils.email import send_email


class RegisterView(View):
    template_name = 'account_module/register.html'

    def get(self, request):
        form = RegisterForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            new_user = User(
                email=email,
                username=email,
                active_email_code=get_random_string(48),
                is_active=False
            )
            new_user.set_password(password)
            new_user.first_name = form.cleaned_data['first_name']
            new_user.last_name = form.cleaned_data['last_name']
            y, m, d = int(form.cleaned_data['year']), int(form.cleaned_data['month']), int(form.cleaned_data['day'])
            new_user.birth_date = datetime.date(y, m, d)
            new_user.gender = form.cleaned_data['gender']
            new_user.save()

            domain = request.get_host()
            activation_link = f"http://{domain}{reverse('active_code', kwargs={'email_active_code': new_user.active_email_code})}"

            send_email(
                subject='Activate your account',
                to=new_user.email,
                context={'user': new_user, 'activation_link': activation_link},
                template_name='email/active_account.html'
            )

            return redirect(reverse("home"))
        context={'form': form}
        return render(request,self.template_name, context)

class ActivateView(View):
    def get(self, request, email_active_code):
        user: User = User.objects.filter(active_email_code__iexact=email_active_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.active_email_code = get_random_string(48)
                user.save()
                return redirect(reverse("home"))
        return render(request, '404_dark.html', status=404)

class LoginView(View):
    template_name = 'account_module/login.html'
    def get(self, request):
        form = LoginForm()
        return render(request, self.template_name, {'form': form})
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            remember_me=form.cleaned_data['remember_me']
            user = User.objects.filter(email__iexact=email).first()
            if user is not None:
                if not user.is_active:
                    form.add_error("email","this email is not active")
                else:
                    if user.check_password(password):
                        login(request, user)
                        if remember_me:
                            request.session.set_expiry(1209600)
                        else:
                            request.session.set_expiry(0)
                        return redirect(reverse("home"))
                    else:
                        form.add_error("email","invalid email or password")
            else:
                form.add_error("email","invalid email or password")
        return render(request, self.template_name, {'form': form})
