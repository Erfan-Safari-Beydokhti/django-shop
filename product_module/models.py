from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.text import slugify

from account_module.models import User


# Create your models here.

def unique_slugify(instance, value, slug_field_name='slug', queryset=None, slug_separator='-'):
    slug = slugify(value)

    if queryset is None:
        queryset = instance.__class__.objects.all()

    original_slug = slug
    index = 1

    while queryset.filter(**{slug_field_name: slug}).exclude(pk=instance.pk).exists():
        slug = original_slug + slug_separator + str(index)
        index += 1

    return slug


class ProductCategory(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name="Title", db_index=True)
    slug = models.SlugField(max_length=100, unique=True, verbose_name="Slug", db_index=True, default="", null=True,
                            blank=True)
    is_active = models.BooleanField(default=True, verbose_name="Active")
    is_delete = models.BooleanField(default=False, verbose_name="Delete")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, self.title)
        super().save(*args, **kwargs)


class ProductBrand(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title", db_index=True)
    slug = models.SlugField(max_length=100, unique=True, verbose_name="Slug", db_index=True, default="", null=True,
                            blank=True)
    is_active = models.BooleanField(default=True, verbose_name="Active")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Product Brand"
        verbose_name_plural = "Product Brands"


class ProductTag(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title", db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Product Tag"
        verbose_name_plural = "Product Tags"


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title", db_index=True)
    category = models.ManyToManyField(ProductCategory, verbose_name="Category", related_name="product_categories")
    tag = models.ManyToManyField(ProductTag, verbose_name="Tag", related_name="product_tags")
    brand = models.ForeignKey(ProductBrand, verbose_name="Brand", on_delete=models.CASCADE,
                              related_name="product_brands", null=True, blank=True)
    image = models.ImageField(upload_to='images/products', verbose_name="Image", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")
    short_description = models.CharField(max_length=255, verbose_name="Short Description", db_index=True)
    description = models.TextField(verbose_name="Description", db_index=True)
    is_active = models.BooleanField(default=False, verbose_name="Active")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="Slug", db_index=True, default="", null=True,
                            blank=True)
    is_delete = models.BooleanField(default=False, verbose_name="Delete")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, self.title)
        super().save(*args, **kwargs)


class ProductGallery(models.Model):
    product = models.ForeignKey(Product, verbose_name="Product", on_delete=models.CASCADE,
                                related_name="product_galleries")
    image = models.ImageField(upload_to='images/products_galley', verbose_name="Image", null=True, blank=True)

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = "Product Gallery"
        verbose_name_plural = "Product Galleries"


class ProductVisit(models.Model):
    product = models.ForeignKey(Product, verbose_name="Product", on_delete=models.CASCADE,
                                related_name="product_visits")
    ip = models.GenericIPAddressField(verbose_name="User-IP", db_index=True)
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.product.title} / {self.ip}"

    class Meta:
        verbose_name = "Product Visit"
        verbose_name_plural = "Product Visits"


class WishList(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE, related_name='wish_list')
    product = models.ForeignKey(Product, verbose_name="Product", on_delete=models.CASCADE, related_name='wishlist_set')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Create at")

    class Meta:
        unique_together = ("user", "product")
        verbose_name = "Wish List"
        verbose_name_plural = "Wish List"

    def __str__(self):
        return f"{self.user} / {self.product}"


class ProductReview(models.Model):
    product = models.ForeignKey(Product, verbose_name="Product", on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField(verbose_name="Review")
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True, verbose_name="Rating",validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Create at")

    def __str__(self):
        return f"{self.user} / {self.product}"
