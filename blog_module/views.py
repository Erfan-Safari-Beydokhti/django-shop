from dbm import error
from http.client import HTTPResponse
from lib2to3.fixes.fix_input import context

from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.views.generic import ListView, DetailView
from django.db.models import Prefetch, Count
from django.contrib import messages

from blog_module.models import Blog, BlogCategory, BlogTag, BlogComment


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
            query = query.filter(tag__slug__iexact=tag_name)

        query = query.filter(is_active=True).select_related('author').prefetch_related('selected_categories')
        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = BlogTag.objects.filter(is_active=True)
        return context


class BlogDetailView(DetailView):
    model = Blog
    context_object_name = 'blog'
    template_name = "blog_module/blog_detail.html"

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        blog = self.get_object()

        context["next_post"] = Blog.objects.filter(
            created_at__gt=blog.created_at, selected_categories__in=blog.selected_categories.all(), is_active=True
        ).exclude(id=blog.id).distinct().order_by("created_at").first()

        context["previous_post"] = Blog.objects.filter(created_at__lt=blog.created_at,
                                                       selected_categories__in=blog.selected_categories.all(),
                                                       is_active=True).exclude(id=blog.id).distinct().order_by(
            "-created_at").first()

        context["comments"] = BlogComment.objects.filter(blog_id=blog.id, parent_id=None).prefetch_related(
            'comments').order_by('-created_at')[:10]  # is_accepted=True
        context["comments_count"] = BlogComment.objects.filter(blog_id=blog.id).count()
        return context


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


def add_blog_comment(request: HttpRequest):
    blog_comment = request.GET.get('blog_comment')
    blog_id = request.GET.get('blog_id')
    parent_id = request.GET.get('parent_id')

    blog = get_object_or_404(Blog, id=blog_id)
    if parent_id:
        parent = BlogComment.objects.filter(id=parent_id).first()
    else:
        parent = None
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in to post a comment.")
    elif not blog_comment:
        messages.warning(request, "Comment text cannot be empty.")
    else:
        BlogComment.objects.create(
            blog=blog,
            text=blog_comment,
            parent=parent,
            user=request.user
        )
        messages.success(request, "Your comment has been submitted successfully.")

    comments = blog.comments.filter(parent__isnull=True).order_by('-created_at')[:10]  # is_accepted=True
    context = {
        'comments': comments.prefetch_related('comments', 'user'),
        'comments_count': blog.comments.count()
    }
    return render(request, 'blog_module/includes/blog_comment_partial.html', context)
