from audioop import reverse

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import ContactForm
# Create your views here.
class ContactView(FormView):
    template_name = 'contact_module/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact-us')


def form_valid(self, form):
    contact=form.save(commit=False)
