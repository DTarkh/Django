
from django.shortcuts import render, redirect
from .models import Book, Category
from .forms import BookForm



def index(request):
    book_name = request.GET.get('book_name')
    category = request.GET.getlist('category')

    if book_name:
        books = Book.objects.filter(title__icontains=book_name)
    elif category:
        books = Book.objects.filter(category__in=category)
    else:
        books = Book.objects.all()




    categories = Category.objects.all()
    book_by_genres = {}


    for category in categories:
        genre = category.genre
        if genre not in book_by_genres:
            book_by_genres[genre] = []
        book_by_genres[genre].append(category)

    print(book_by_genres)

    return render(request, 'index.html', {'books': books, 'book_by_genres': book_by_genres})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()
        return redirect('bookshop:index')

    else:
        form = BookForm()
        return render(request, 'add_book.html', {'form': form})