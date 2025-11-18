from http.client import HTTPResponse
from lib2to3.fixes.fix_input import context

from django.contrib.auth.views import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from django.template.loader import render_to_string
from django.contrib import messages
from cart_module.models import Cart, CartItem
from product_module.models import Product
from django.contrib import messages

# Create your views here.

@login_required()
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, item_created = CartItem.objects.get_or_create(product=product, cart=cart)
    quantity = int(request.POST.get('quantity', 1))
    if not item_created:
        cart_item.quantity += quantity
    else:
        cart_item.quantity = quantity
    cart_item.save()
    messages.success(request, 'Your cart has been updated')
    return redirect('product-detail-view', slug=product.slug)


@login_required()
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = existitems(request, cart)
    sub_total=float(cart.total_price())
    tax=round(sub_total*0.0005,2)
    grand_total=sub_total+tax
    context = {
        'cart': cart,
        'cart_items': cart_items,
        'sub_total': sub_total,
        'tax': tax,
        'grand_total': grand_total,


    }
    return render(request, 'cart_module/cart.html', context)


@login_required()
def remove_from_cart(request):
    item_id = request.GET.get('item_id')
    if not item_id:
        return JsonResponse({'status': 'not_found_item_id'})

    remove_count, remove = CartItem.objects.filter(id=item_id, cart__user=request.user).delete()
    if not remove_count:
        return JsonResponse({'status': 'not_found_item_id'})
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)

    context = {
        'cart': cart,
        'cart_items': cart_items,
    }
    return JsonResponse({
        'status': 'success',
        'data': render_to_string('cart_module/cart_item.html', context),
    })


@login_required()
def change_cart_detail(request):
    item_id = request.GET.get('item_id')
    state = request.GET.get('state')
    if item_id is None or state is None:
        return JsonResponse({
            'status': 'not_found_detail_id_or_state'
        })
    item = CartItem.objects.filter(id=item_id, cart__user=request.user).first()
    if item is None:
        return JsonResponse({
            'status': 'not_found_detail_id_or_state'
        })
    if state == 'decrease':
        if item.quantity == 1:
            item.delete()
        else:
            item.quantity -= 1
            item.save()
    elif state == 'increase':
        item.quantity += 1
        item.save()
    else:
        return JsonResponse({
            'status': 'not_found_detail_id_or_state'
        })
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    context = {
        'cart': cart,
        'cart_items': cart_items,
    }
    return JsonResponse(
        {'status': 'success',
         'data': render_to_string('cart_module/cart_item.html', context),
         }
    )


def clear_cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart.items.all().delete()
    return redirect(cart_detail)


def existitems(request, cart):
    if cart.items.exists():
        return CartItem.objects.filter(cart=cart, cart__user=request.user)
    else:
        messages.error(request, 'No cart items')




