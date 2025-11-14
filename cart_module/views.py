from lib2to3.fixes.fix_input import context

from django.contrib.auth.views import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from django.template.loader import render_to_string

from cart_module.models import Cart, CartItem
from product_module.models import Product
from django.contrib import messages

# Create your views here.

@login_required()
def add_to_cart(request, product_id):
    product=get_object_or_404(Product, id=product_id)
    cart,created = Cart.objects.get_or_create(user=request.user)
    cart_item,created = CartItem.objects.get_or_create(product=product,cart=cart)
    quantity=int(request.POST.get('quantity',1))
    if not created:
        cart_item.quantity += quantity
    else:
        cart_item.quantity = quantity
    cart_item.save()
    messages.success(request, 'Your cart has been updated')
    return redirect('product-detail-view', slug=product.slug)


@login_required()
def cart_detail(request):
    cart,created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    context={
        'cart':cart,
        'cart_items':cart_items,
    }
    return render(request,'cart_module/cart.html',context)

@login_required()
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id,cart__user=request.user)
    item.delete()
    return redirect('cart_detail')

@login_required()
def change_cart_detail(request):
    item_id=request.GET.get('item_id')
    state=request.GET.get('state')
    if item_id is None or state is None:
        return JsonResponse({
            'status':'not_found_detail_id_or_state'
        })
    item=CartItem.objects.filter(id=item_id,cart__user=request.user).first()
    if item is None:
        return JsonResponse({
            'status':'not_found_detail_id_or_state'
        })
    if state == 'decrease':
        if item.quantity ==1:
            item.delete()
        else:
            item.quantity -= 1
            item.save()
    elif state == 'increase':
        item.quantity += 1
        item.save()
    else:
        return JsonResponse({
            'status':'not_found_detail_id_or_state'
        })
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    context={
        'cart':cart,
        'cart_items':cart_items,
    }
    return JsonResponse(
        {'status': 'success',
         'data': render_to_string('cart_module/cart_item.html',context),
         }
    )