from django.db import models
from account_module.models import User
from product_module.models import Product


# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='User',related_name='cart')
    created = models.DateTimeField(auto_now_add=True,verbose_name='Created')
    updated = models.DateTimeField(auto_now=True,verbose_name='Updated')

    def __str__(self):
        return f"{self.id} , {self.user}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,verbose_name='Cart',related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,verbose_name='Product',related_name='items')
    quantity = models.PositiveIntegerField(verbose_name='Quantity',default=1)

    def __str__(self):
        return f"{self.quantity} x {self.quantity}"

    def total_price(self):
        return self.product.price  self.quantity
