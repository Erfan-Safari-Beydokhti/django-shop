from django.urls import path
from .views import TrackOrderView,OrderListView,OrderDetailView
urlpatterns = [
    path("track/", TrackOrderView.as_view(), name="track-order"),
    path("", OrderListView.as_view(), name="my-orders"),
    path("order/<str:order_id>/", OrderDetailView.as_view(), name="order-detail"),
]