from django.contrib import admin

from order_module.models import Order, OrderItem
from product_module.models import Product

# Register your models here.


admin.site.register(Order)
admin.site.register(OrderItem)