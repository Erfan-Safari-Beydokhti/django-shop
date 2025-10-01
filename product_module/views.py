from itertools import product

from django.db.models import Prefetch, Count
from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import ListView

from product_module.models import Product, ProductCategory, ProductBrand


# Create your views here.


class ProductListView(ListView):
    template_name = 'product_module/product_list.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 4
    ordering = ["-price"]

    def get_queryset(self):
        query=super(ProductListView, self).get_queryset()
        category_name=self.kwargs.get('cat')
        price_min=self.request.GET.get('price_min')
        price_max=self.request.GET.get('price_max')
        if category_name is not None:
            query=query.filter(category__slug__iexact=category_name)
        if price_min is not None:
            query=query.filter(price__gte=price_min)
        if price_max is not None:
            query=query.filter(price__lte=price_max)
        return query
def product_categories_component(request:HttpRequest):
    main_categories=ProductCategory.objects.annotate(products_count=Count("product_categories")).filter(parent=None,is_active=True).prefetch_related(Prefetch('children',queryset=ProductCategory.objects.filter(is_active=True)))
    context={'main_categories':main_categories}
    return render(request,'product_module/component/product_categories_component.html',context)

def product_brands_component(request:HttpRequest):
    brand=ProductBrand.objects.filter(is_active=True)
    context={'brand':brand}
    return render(request,'product_module/component/product_brands_component.html',context)