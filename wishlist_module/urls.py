from django.urls import path
from .views import WishListView, WishDeleteItemView, clear_wishlist

urlpatterns=[
    path('',WishListView.as_view(),name='wishlist'),
    path('remove-wish-item',WishDeleteItemView.as_view(),name='remove-wish-item'),
    path('clear-wishlist',clear_wishlist,name='clear-wish-list'),
]