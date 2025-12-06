from product_module.models import ProductCategory


def header_categories(request):
    return {
        'categories':ProductCategory.objects.all(),
    }