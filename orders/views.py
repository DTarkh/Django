from django.shortcuts import render, redirect
from .models import Cart, CartItem
from django.contrib.auth.decorators import login_required
from bookshop.models import Book



@login_required(login_url='/users/login')
def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)

    total_amount = sum(cart_item.total for cart_item in cart_items)



    return render(request, 'cart.html', {'cart': cart, 'cart_items': cart_items, 'total_amount': total_amount})


@login_required(login_url='/users/login')
def add_cart_item(request, pk):
    book = Book.objects.get(pk=pk)

    cart, created = Cart.objects.get_or_create(user=request.user)

    if book.stock > 0:
        cart_item, cart_item_created = CartItem.objects.get_or_create(cart=cart, book=book)

        if not cart_item_created:
            cart_item.quantity += 1
        else:
            cart_item.quantity = 1
        cart_item.save()

    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/users/login')
def update_cart_item(request, pk):
    if request.method == "POST":
        cart_item = CartItem.objects.get(pk=pk)

        new_quantity = int(request.POST.get('quantity'))

        if new_quantity == 0:
            cart_item.delete()

        elif new_quantity > cart_item.book.stock:
            cart_item.quantity = new_quantity
            cart_item.save()

    return redirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='/users/login')
def delete_cart_item(request, pk):
    cart_item = CartItem.objects.get(pk=pk)

    cart_item.delete()


    return redirect(request.META.get('HTTP_REFERER'))
