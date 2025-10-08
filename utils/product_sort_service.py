from django.db.models import Count, Avg

from product_module.models import Product


class ProductSortService:
    @staticmethod
    def get_product_context(sort):
        products_qs = Product.objects.filter(is_active=True,is_delete=False)

        if sort == 'Visit':
            products_qs = products_qs.annotate(visit_count=Count('product_visits')).order_by('-visit_count')
        elif sort == 'Rating':
            products_qs = products_qs.annotate(avg_rating=Avg('reviews__rating')).order_by('-avg_rating')
        elif sort == 'Lowest_p':
            products_qs = products_qs.order_by('price')
        elif sort == 'Highest_p':
            products_qs = products_qs.order_by('-price')
        elif sort == 'Latest':
            products_qs=products_qs.order_by('id')
        else:
            products_qs = products_qs.order_by('-id')
        return products_qs


