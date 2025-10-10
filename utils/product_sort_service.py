from django.db.models import Count, Avg

from product_module.models import Product


class ProductSortService:
    @staticmethod
    def get_product_context(queryset, sort):
        if sort == 'Visit':
            queryset = queryset.annotate(visit_count=Count('product_visits')).order_by('-visit_count')
        elif sort == 'Rating':
            queryset = queryset.annotate(avg_rating=Avg('reviews__rating')).order_by('-avg_rating')
        elif sort == 'Lowest_p':
            queryset = queryset.order_by('price')
        elif sort == 'Highest_p':
            queryset = queryset.order_by('-price')
        elif sort == 'Latest':
            queryset = queryset.order_by('id')
        else:
            queryset = queryset.order_by('-id')
        return queryset


