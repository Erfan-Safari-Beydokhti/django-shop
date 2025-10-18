from django.urls import path
from .views import BlogListView, BlogDetailView,add_blog_comment

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('cat/<str:cat>', BlogListView.as_view(), name='blog-category-list-view'),
    path('tag/<str:tag>', BlogListView.as_view(), name='blog-tag-list-view'),
    path('add-blog-comment' ,add_blog_comment, name='add-blog-comment'),
    path('<slug:slug>' , BlogDetailView.as_view(), name='blog-detail'),
    path('load-more-comment' , load_more_comment, name='load-more-comment'),
]
