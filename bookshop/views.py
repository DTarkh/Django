
from django.shortcuts import render, redirect
from .models import Book, Category
from .forms import BookForm



def index(request):
    books = Book.objects.all()
    return render(request, 'index.html', {'books': books})




def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()
        return redirect('/bookshop')

    else:
        form = BookForm()
        return render(request, 'add_book.html', {'form': form})