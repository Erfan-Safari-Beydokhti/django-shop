from lib2to3.fixes.fix_input import context
from tempfile import template

from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.generic import TemplateView, View

from home_module.models import HomeSlider
from product_module.models import ProductCategory, Product


# Create your views here.
class IndexView(TemplateView):
    template_name = 'home_module/index_page.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['slider']=HomeSlider.objects.filter(is_active=True)
        context["electronic_categories"]=ProductCategory.objects.filter(is_active=True,show_on_home=True)[:4]
        context["phones"]=Product.objects.prefetch_related("category").filter(is_active=True,category__slug='phone')[:6]
        context["laptops"]=Product.objects.prefetch_related("category").filter(is_active=True,category__slug='laptop')[:6]
        return context

class HomeProductTabAjaxView(View):
    def get(self, request, *args, **kwargs):
        category=request.GET.get('category')
        sort=request.GET.get('sort','Newest')
        template = request.GET.get('template')

        qs=Product.objects.filter(category__slug=category,is_active=True).distinct()

        if sort == 'Newest':
            qs = qs.order_by('-id')
        elif sort == 'Latest':
            qs = qs.order_by('id')
        elif sort == 'Visit':
            qs = qs.order_by('-product_visits')
        elif sort == 'Rating':
            qs = qs.order_by('-reviews')
        elif sort == 'Lowest_p':
            qs = qs.order_by('price')
        elif sort == 'Highest_p':
            qs = qs.order_by('-price')

        products=qs[:8]
        html = render_to_string(f'home_module/includes/{template}',
            {'products': products},
            request=request
        )
        return JsonResponse({'html':html})