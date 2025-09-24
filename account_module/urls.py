from django.urls import path
from .views import RegisterView, ActivateView

urlpatterns = [
    path('register/',RegisterView.as_view(),name='register_view'),
    path('active_code/<email_active_code>/', ActivateView.as_view(), name='active_code'),
    path('login', ActivateView.as_view(), name='login_view'),
]