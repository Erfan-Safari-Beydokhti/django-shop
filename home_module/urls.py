from django.urls import path

from home_module.views import IndexView

urlpatterns = [
    path('',IndexView.as_view(), name='home'),
]