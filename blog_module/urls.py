from django.urls import path
from .views import BlogListView, BlogDetailView

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('cat/<str:cat>', BlogListView.as_view(), name='blog-category-list-view'),
    path('tag/<str:tag>', BlogListView.as_view(), name='blog-tag-list-view'),
    path('<slug:slug>' , BlogDetailView.as_view(), name='blog-detail'),
    path('add-blog-comment' , BlogDetailView.as_view(), name='add-blog-comment'),
]
