from django.db import models

from account_module.models import User


# Create your models here.
class ContactMessages(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='User',related_name='messages')
    subject = models.CharField(max_length=100,verbose_name='Subject')
    message = models.TextField(verbose_name='Message')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    def __str__(self):
        return self.subject
    class Meta:
        verbose_name_plural = 'Contact Messages'
        verbose_name = 'Contact Message'