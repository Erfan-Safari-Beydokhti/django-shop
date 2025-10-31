from django.urls import path

from .views import dash_address_book, dash_address_edit, dash_address_add, dash_edit_profile, \
    dash_my_profile, dash_cancellation, dash_my_order, dash_manage_order, dash_track_order, dash_address_make_default, \
    dashboard

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('dash-address-book/', dash_address_book, name='dash-address-book'),
    path('dash-address-edit/', dash_address_edit, name='dash-address-edit'),
    path('dash-address-add/', dash_address_add, name='dash-address-add'),
    path('dash-edit-profile/', dash_edit_profile, name='dash-edit-profile'),
    path('dash-my-profile/', dash_my_profile, name='dash-my-profile'),
    path('dash-cancellation/', dash_cancellation, name='dash-cancellation'),
    path('dash-my-order/', dash_my_order, name='dash-my-order'),
    path('dash-track-order/', dash_track_order, name='dash-track-order'),
    path('dash-address-make-default/', dash_address_make_default, name='dash-address-make-default'),
    path('dash-manage-order/', dash_manage_order, name='dash-manage-order'),

]
