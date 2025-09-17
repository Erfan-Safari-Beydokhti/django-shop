from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class IndexView(TemplateView):
    template_name = 'home_module/index_page.html'

class Header_component(TemplateView):
    template_name = 'shared/site_header_component.html'

class Footer_component(TemplateView):
    template_name = 'shared/site_footer_component.html'