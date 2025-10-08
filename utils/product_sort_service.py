from django.db.models import Count, Min, Max

from product_module.models import Product


class ProductSortService:
    @staticmethod
    def get_product_context(sort):
        products_qs = Product.objects.filter(is_active=True,is_delete=False)

        if sort == 'Visit':
            products_qs = products_qs.annotate(visit_count=Count('visit')).order_by('-visit_count')
        elif sort == 'Rating':
            products_qs = products_qs.annotate(rating_count=Count('rating')).order_by('-rating_count')
        elif sort == 'Lowest_p':
            products_qs = products_qs.annotate(lowest_p=Min('price')).order_by('lowest_p')
        elif sort == 'Highest_p':
            products_qs = products_qs.annotate(highest_p=Max('price')).order_by('highest_p')
        elif sort == 'Latest':
            products_qs=products_qs.order_by('id')
        else:
            products_qs = products_qs.order_by('-id')
        return products_qs


