from django.db import models

# Create your models here.

class BlogCategory(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE , verbose_name='Parent category')
    title = models.CharField(max_length=200, verbose_name='Category title')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='Slug',db_index=True,default='',null=True,blank=True)
    is_active = models.BooleanField(default=True, verbose_name='Is active')

