from django.shortcuts import render
from django.views.generic import TemplateView

from home_module.models import HomeSlider
from product_module.models import ProductCategory


# Create your views here.
class IndexView(TemplateView):
    template_name = 'home_module/index_page.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['slider']=HomeSlider.objects.filter(is_active=True)
        context["electronic_categories"]=ProductCategory.objects.filter(is_active=True,show_on_home=True)[:4]
        return context