"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_module.urls'), name='index-page'),
    path('', include('account_module.urls'), name='account-page'),
    path('products/', include('product_module.urls'), name='product-page'),
    path('blogs/', include('blog_module.urls'), name='blog-page'),
    path('about/', include('about_module.urls'), name='about-page'),
    path('contact-us/', include('contact_module.urls'), name='contact-page'),
    path('dashboard/', include('dashboard_module.urls'), name='dashboard-page'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
