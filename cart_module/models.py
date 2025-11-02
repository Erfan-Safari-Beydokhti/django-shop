from django.db import models
from account_module.models import User
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='User',related_name='cart')
    created = models.DateTimeField(auto_now_add=True,verbose_name='Created')
    updated = models.DateTimeField(auto_now=True,verbose_name='Updated')

    def __str__(self):
        return f"{self.id} , {self.user}"


