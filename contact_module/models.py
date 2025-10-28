from django.db import models

from account_module.models import User


# Create your models here.
class ContactMessages(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.subject
    class Meta:
        verbose_name_plural = 'Contact Messages'
        verbose_name = 'Contact Message'