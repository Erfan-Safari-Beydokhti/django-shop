from lib2to3.fixes.fix_input import context

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch, Count
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from product_module.models import Product, ProductCategory, ProductBrand, WishList, ProductReview, ProductVisit
from utils.http_service import get_user_ip
from utils.review_service import ReviewService


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

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        product = self.get_object()
        sort = self.request.GET.get('sort', 'best')
        reviews_qs = ProductReview.objects.filter(product_id=product.id, is_accepted=True)

        if sort == 'worse':
            reviews_qs = reviews_qs.order_by('rating')
        else:
            reviews_qs = reviews_qs.order_by('-rating')

        context['reviews'] = reviews_qs
        context['reviews_count'] = reviews_qs.count()
        context['sort'] = sort

        user_ip = get_user_ip(self.request)
        user_id = None
        if self.request.user.is_authenticated:
            user_id = self.request.user.id
        has_been_visit = ProductVisit.objects.filter(ip__iexact=user_ip, product_id=product.id).exists()
        if not has_been_visit:
            new_visit = ProductVisit(product_id=product.id, ip=user_ip, user_id=user_id)
            new_visit.save()

        return context


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

        try:
            rating = int(rating)
        except (TypeError, ValueError):
            messages.error(request, "Invalid rating value.")
            return redirect('product-detail-view', slug=product.slug)

        if not (1 <= rating <= 5):
            messages.error(request, "Rating must be between 1 and 5.")
            return redirect('product-detail-view', slug=product.slug)

        if not text.strip():
            messages.error(request, "Please write your review text.")
            return redirect('product-detail-view', slug=product.slug)

        if ProductReview.objects.filter(user=request.user, product=product).exists():
            messages.warning(request, "You have already submitted a review for this product.")
            return redirect('product-detail-view', slug=product.slug)

        ProductReview.objects.create(
            user=request.user,
            product=product,
            rating=rating,
            text=text
        )

        messages.success(request, "Your review has been submitted successfully!")
        return redirect('product-detail-view', slug=product.slug)

    return redirect('product-detail-view', slug=product.slug)


def product_reviews_component(request, product_id):
    sort = request.GET.get('sort', 'best')
    product = get_object_or_404(Product, id=product_id)
    context = ReviewService.get_review_context(product, sort)
    context["product"] = product
    return render(request, 'product_module/includes/product_review_partial.html', context)
