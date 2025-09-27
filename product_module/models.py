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


class ProductTag(models.Model):
    title=models.CharField(max_length=100,verbose_name="Title",db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="Product Tag"
        verbose_name_plural="Product Tags"


class Product(models.Model):
    title=models.CharField(max_length=100,verbose_name="Title",db_index=True)
    category=models.ManyToManyField(ProductCategory,verbose_name="Category",on_delete=models.CASCADE,related_name="product_categories")
    tag=models.ManyToManyField(ProductTag,verbose_name="Tag",on_delete=models.CASCADE,related_name="product_tags")
    brand=models.ForeignKey(ProductBrand,verbose_name="Brand",on_delete=models.CASCADE,related_name="product_brands",null=True,blank=True)
    image=models.ImageField(upload_to='images/products',verbose_name="Image",null=True,blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2,verbose_name="Price")
    short_description=models.CharField(max_length=255,verbose_name="Short Description",db_index=True)
    description=models.TextField(verbose_name="Description",db_index=True)
    is_active=models.BooleanField(default=False,verbose_name="Active")
    slug=models.SlugField(max_length=100,unique=True,verbose_name="Slug",db_index=True,default="",null=True,blank=True)
    is_delete=models.BooleanField(default=False,verbose_name="Delete")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="Product"
        verbose_name_plural="Products"

