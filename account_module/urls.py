from django.urls import path
from .views import RegisterView, ActivateView, LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login_view'),
    path('register/',RegisterView.as_view(),name='register_view'),
    path('active_code/<email_active_code>/', ActivateView.as_view(), name='active_code'),
]
