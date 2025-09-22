from django.db import models

# Create your models here.


class User(models.Model):
    avatar = models.ImageField(upload_to='images/profile',verbose_name='User Profile',null=True,blank=True)
    active_email_code=models.CharField(max_length=100,verbose_name='Email Code')
    about_user=models.TextField(null=True,blank=True,verbose_name='About User')

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

