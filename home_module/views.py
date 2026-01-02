from django.db.models import Count
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.generic import TemplateView, View

from blog_module.models import Blog
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
        context["blogs"]=Blog.objects.filter(is_active=True).annotate(comments_count=Count('comments')).select_related('author').prefetch_related('selected_categories','tag').order_by('-created_at')[:3]
        return context

