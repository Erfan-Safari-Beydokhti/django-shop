from django.urls import path

from faq_module.views import FAQView

urlpatterns = [
    path('',FAQView.as_view(),name='faq-temp'),
]