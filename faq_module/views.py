from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


class FAQView(TemplateView):
    template_name = 'faq_module/faq_page.html'
