from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import ListView

from product_module.models import Product, ProductCategory


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
        if category_name is not None:
            query=query.filter(category__slug__iexact=category_name)
        return query
def product_categories_component(request:HttpRequest):
    main_categories=ProductCategory.objects.filter(parent=None,is_active=True).prefetch_related('children')
    context={'main_categories':main_categories}
    return render(request,'product_module/component/product_categories_component.html',context)
