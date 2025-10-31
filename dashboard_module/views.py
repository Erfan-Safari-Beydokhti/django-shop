from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request,'dashboard_module/dashboard.html')
def dash_address_add(request):
    return render(request,'dashboard_module/dash_address_add.html')
def dash_address_edit(request):
    return render(request,'dashboard_module/dash_address_edit.html')
def dash_address_book(request):
    return render(request,'dashboard_module/dash_address_book.html')
def dash_address_make_default(request):
    return render(request,'dashboard_module/dash_address_make_default.html')
def dash_cancellation(request):
    return render(request,'dashboard_module/dash_cancellation.html')
def dash_edit_profile(request):
    return render(request,'dashboard_module/dash_edit_profile.html')
def dash_manage_order(request):
    return render(request,'dashboard_module/dash_manage_order.html')
def dash_my_order(request):
    return render(request,'dashboard_module/dash_my_order.html')
def dash_my_profile(request):
    return render(request,'dashboard_module/dash_my_profile.html')
def dash_track_order(request):
    return render(request,'dashboard_module/dash_track_order.html')