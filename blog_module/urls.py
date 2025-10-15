from django.urls import path
from .views import BlogListView

urlpatterns=[
    path('',BlogListView.as_view(),name='blog_list'),
    path('cat/<str:cat>',BlogListView.as_view(),name='blog-category-list-view'),

]