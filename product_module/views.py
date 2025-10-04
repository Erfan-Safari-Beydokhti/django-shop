from itertools import product

from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch, Count
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from pyexpat.errors import messages

from product_module.forms import ReviewForm
from product_module.models import Product, ProductCategory, ProductBrand, WishList, ProductReview


# Create your views here.


class ProductListView(ListView):
    template_name = 'product_module/product_list.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 4
    ordering = ["-price"]

    def get_queryset(self):
        query = super(ProductListView, self).get_queryset()
        category_name = self.kwargs.get('cat')
        brand_name = self.kwargs.get('brand')
        price_min = self.request.GET.get('price_min')
        price_max = self.request.GET.get('price_max')
        if category_name is not None:
            query = query.filter(category__slug__iexact=category_name)
        if price_min is not None:
            query = query.filter(price__gte=price_min)
        if price_max is not None:
            query = query.filter(price__lte=price_max)
        if brand_name is not None:
            query = query.filter(brand__slug__iexact=brand_name)
        return query


class ProductDetailView(DetailView):
    template_name = 'product_module/product_detail.html'
    model = Product
    context_object_name = 'product'


def product_categories_component(request: HttpRequest):
    main_categories = ProductCategory.objects.annotate(products_count=Count("product_categories")).filter(parent=None,
                                                                                                          is_active=True).prefetch_related(
        Prefetch('children', queryset=ProductCategory.objects.filter(is_active=True)))
    context = {'main_categories': main_categories}
    return render(request, 'product_module/component/product_categories_component.html', context)


def product_brands_component(request: HttpRequest):
    brand = ProductBrand.objects.annotate(products_count=Count("product_brands")).filter(is_active=True)
    context = {'brand': brand}
    return render(request, 'product_module/component/product_brands_component.html', context)


@login_required
def add_to_wishlist(request: HttpRequest, product_id):
    product = get_object_or_404(Product, id=product_id)
    WishList.objects.create(user=request.user, product=product)
    return redirect('product-detail-view', slug=product.slug)


@login_required
def add_review(request: HttpRequest, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        rating = request.POST.get("rating")
        text = request.POST.get("text")

        if rating and text:
            ProductReview.objects.create(user=request.user, product=product, rating=rating, text=text)
        return redirect('product-detail-view', slug=product.slug)
    return redirect('product-detail-view', slug=product.slug)
