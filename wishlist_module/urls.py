from django.urls import path
from .views import WishListView,WishDeleteItemView
urlpatterns=[
    path('',WishListView.as_view(),name='wishlist'),
    path('remove-wish-item',WishDeleteItemView.as_view(),name='remove-wish-item'),
]