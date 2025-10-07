from product_module.models import ProductReview


class ReviewService:
    @staticmethod
    def get_review_context(product,sort='best'):
        reviews_qs=ProductReview.objects.filter(product_id=product.id,is_active=True)

        if sort=='worse':
            reviews_qs=reviews_qs.order_by('rating')
        else:
            reviews_qs=reviews_qs.order_by('-rating')

        return {
            'reviews': reviews_qs,
            'reviews_count': reviews_qs.count(),
            'sort': sort

        }