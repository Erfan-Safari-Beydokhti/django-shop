from django.db import models

# Create your models here.


class ProductCategory(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    title= models.CharField(max_length=100,verbose_name="Title",db_index=True)
    url_title=models.CharField(max_length=150,verbose_name="URL Title",db_index=True)
    is_active=models.BooleanField(default=True,verbose_name="Active")
    is_delete=models.BooleanField(default=False,verbose_name="Delete")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="Product Category"
        verbose_name_plural="Product Categories"

class ProductBrand(models.Model):
    title=models.CharField(max_length=100,verbose_name="Title",db_index=True)
    url_title=models.CharField(max_length=150,verbose_name="URL Title",db_index=True)
    is_active=models.BooleanField(default=True,verbose_name="Active")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="Product Brand"
        verbose_name_plural="Product Brands"
