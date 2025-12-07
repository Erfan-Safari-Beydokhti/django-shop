from product_module.models import ProductCategory


def header_categories(request):
    return {
        'categories':ProductCategory.objects.filter(is_active=True,is_delete=False,parent__isnull=True),
    }