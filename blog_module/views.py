from lib2to3.fixes.fix_input import context

from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Prefetch, Count
from blog_module.models import Blog, BlogCategory, BlogTag


# Create your views here.


class BlogListView(ListView):
    model = Blog
    context_object_name = 'blogs'
    template_name = "blog_module/blog_list.html"
    paginate_by = 4
    ordering = ['-created_at']

    def get_queryset(self):
        query = super(BlogListView, self).get_queryset()
        category_name = self.kwargs.get('cat')
        search = self.request.GET.get('search')
        tag_name = self.kwargs.get('tag')
        if category_name is not None:
            query = query.filter(selected_categories__slug__iexact=category_name)
        if search is not None:
            query = query.filter(title__icontains=search)
        if tag_name is not None:
            query = query.filter(tag__title__iexact=tag_name)

        query = query.filter(is_active=True).prefetch_related('selected_categories', 'author')
        return query


class BlogDetailView(DetailView):
    model = Blog
    context_object_name = 'blog'
    template_name = "blog_module/blog_detail.html"


def blog_categories_component(request: HttpRequest):
    main_categories = BlogCategory.objects.annotate(blog_count=Count('blogs')).filter(is_active=True,
                                                                                      parent=None).prefetch_related(
        Prefetch('children', queryset=BlogCategory.objects.filter(is_active=True)))
    context = {'main_categories': main_categories}
    return render(request, 'blog_module/component/blog_categories_component.html', context)


def blog_recent_post_component(request: HttpRequest):
    recent_post = Blog.objects.filter(is_active=True).order_by('-created_at')[:3]
    context = {'recent_post': recent_post}
    return render(request, 'blog_module/component/blog_recent_post_component.html', context)

def blog_tags_component(request: HttpRequest):
    tags = BlogTag.objects.filter(is_active=True)
    context = {'tags': tags}
    return render(request, 'blog_module/component/blog_tags_component.html', context)

