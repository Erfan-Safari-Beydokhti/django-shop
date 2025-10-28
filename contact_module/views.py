from audioop import reverse
from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from utils.email import send_email
from .forms import ContactForm
# Create your views here.
class ContactView(FormView):
    template_name = 'contact_module/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact-us')

    def form_valid(self, form):
        contact=form.save(commit=False)
        contact.user=self.request.user
        contact.save()
        send_email('Contact Message', to=self.request.user.email,context={'user':self.request.user},
                   template_name='email/contact_message.html')

        return super(ContactView, self).form_valid(form)

