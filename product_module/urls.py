from django.urls import path
from .views import ProductListView
urlpatterns = [
    path('', ProductListView.as_view(), name='product-list-view'),
    path('cat/<str:cat>', ProductListView.as_view(), name='product-category-list-view'),
]