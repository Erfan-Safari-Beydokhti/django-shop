from django.db import models

from account_module.models import User
from utils.unique_slugify_service import unique_slugify


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

class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='Slug',db_index=True,default='',null=True,blank=True)
    image=models.ImageField(upload_to='images/blogs', verbose_name='Image' ,null=True,blank=True)
    short_description = models.TextField(verbose_name='Short description',null=True,blank=True)
    text = models.TextField(verbose_name='Text',null=True,blank=True)
    selected_categories=models.ManyToManyField(BlogCategory,verbose_name='Selected category',related_name='blogs')
    author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='Author',related_name='blogs',null=True,blank=True,editable=False)
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Created at',editable=False)
    is_active = models.BooleanField(default=True, verbose_name='Is active')

