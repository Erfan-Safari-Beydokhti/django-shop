from django.urls import path

from home_module.views import IndexView, HomeProductTabAjaxView

urlpatterns = [
    path('',IndexView.as_view(), name='home'),
    path('ajax',HomeProductTabAjaxView.as_view(), name='home-products-ajax'),

]