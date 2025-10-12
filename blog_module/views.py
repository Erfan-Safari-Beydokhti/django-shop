from django.shortcuts import render
from django.views.generic import ListView


# Create your views here.


def index(request):
    return render(request,'blog_module/blog_list.html')