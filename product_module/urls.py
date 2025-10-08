from django.urls import path
from .views import ProductListView, ProductDetailView, add_to_wishlist, add_review, product_reviews_component

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list-view'),
    path('cat/<str:cat>/', ProductListView.as_view(), name='product-category-list-view'),
    path('brand/<str:brand>/', ProductListView.as_view(), name='product-brand-list-view'),
    path('products-sort/partial/', ProductListView.as_view(), name='product-sort-partial'),
    path('wishlist/add/<int:product_id>', add_to_wishlist, name='add_to_wishlist'),
    path('<int:product_id>/reviews_partial/', product_reviews_component, name='product-review-partial'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='product-detail-view'),
    path('product/<int:product_id>/add_review', add_review, name='product-review-view'),
]
