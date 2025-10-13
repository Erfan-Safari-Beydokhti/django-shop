from django.db import models
from product_module.models import unique_slugify
# Create your models here.

class BlogCategory(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE , verbose_name='Parent category')
    title = models.CharField(max_length=200, verbose_name='Category title')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='Slug',db_index=True,default='',null=True,blank=True)
    is_active = models.BooleanField(default=True, verbose_name='Is active')

    class Meta:
        verbose_name = 'Blog category'
        verbose_name_plural = 'Blog categories'
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self,self.title)
        super(BlogCategory,self).save(*args, **kwargs)

