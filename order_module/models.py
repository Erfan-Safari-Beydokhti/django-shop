from django.db import models

from account_module.models import User
from product_module.models import Product


# Create your models here.

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('canceled', 'Canceled'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', verbose_name='user')
    created = models.DateTimeField(auto_now_add=True,verbose_name='created')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0,verbose_name='total price')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending',verbose_name='status')
    payment_tracking_code = models.CharField(max_length=200, blank=True, null=True,verbose_name='payment tracking code')

    def __str__(self):
        return f"Order {self.id} - {self.user}"

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def get_total_price(self):
        return self.total_price

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name='order')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items', verbose_name='product')
    quantity = models.PositiveIntegerField(verbose_name='quantity', default=1)
    price_at_purchase = models.DecimalField(max_digits=10, decimal_places=2, default=0,verbose_name='price at purchase')

    def __str__(self):
        return f"{self.product.title} - {self.quantity}"

    class Meta:
        verbose_name = 'Order item'
        verbose_name_plural = 'Order items'

    @property
    def total_price(self):
        return self.quantity * self.price_at_purchase


