from django.shortcuts import render
from .models import Cart, CartItem
from django.contrib.auth.decorators import login_required




@login_required(login_url='/users/login')
def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)

    return render(request, 'cart.html', {'cart': cart, 'cart_items': cart_items})

