from django.urls import path
from .views import ProductListView, ProductDetailView

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list-view'),
    path('cat/<str:cat>/', ProductListView.as_view(), name='product-category-list-view'),
    path('brand/<str:brand>/', ProductListView.as_view(), name='product-brand-list-view'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='product-detail-view'),
]