from django.db import models

# Create your models here.


class About(models.Model):
    title = models.CharField(max_length=100,verbose_name='Title')
    description = models.TextField(verbose_name='Description')


