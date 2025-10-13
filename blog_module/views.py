from django.shortcuts import render
from django.views.generic import ListView

from blog_module.models import Blog, BlogCategory


# Create your views here.


class BlogListView(ListView):
    model = Blog
    context_object_name = 'blogs'
    template_name = "blog_module/blog_list.html"
    paginate_by = 4
    ordering = ['-created_at']

    def get_queryset(self):
        query=super(BlogListView, self).get_queryset()
        query=query.filter(is_active=True).prefetch_related('selected_categories','author')
        return query

