from django.db import models

from account_module.models import User


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
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='orders',verbose_name='user')
    created = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    payment_tracking_code = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"Order {self.id} - {self.user}"

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'




