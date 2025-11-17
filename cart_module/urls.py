from django.urls import path
from .views import cart_detail,remove_from_cart,add_to_cart,change_cart_detail,clear_cart,calculateshopping
urlpatterns=[
    path('',cart_detail,name='cart_detail'),
    path('add/<int:product_id>',add_to_cart,name='add_to_cart'),
    path('remove-cart-item',remove_from_cart,name='remove_from_cart'),
    path('change-cart-item',change_cart_detail,name='change_cart_detail'),
    path('clear-cart',clear_cart,name='clear_cart'),
    path('calculate-shipping',calculateshopping,name='calculate_shipping')
]