from django.db import models

# Create your models here.

from account_module.models import User
from product_module.models import Product


class WishList(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE, related_name='wish_list')
    product = models.ForeignKey(Product, verbose_name="Product", on_delete=models.CASCADE, related_name='products_wish')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Create at")

    class Meta:
        unique_together = ("user", "product")
        verbose_name = "Wish List"
        verbose_name_plural = "Wish List"

    def __str__(self):
        return f"{self.user} / {self.product}"