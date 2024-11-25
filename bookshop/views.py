
from django.shortcuts import render, redirect
from .models import Book, Category
from .forms import BookForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage



def index(request):
    book_name = request.GET.get('book_name')
    category = request.GET.getlist('category')

    if book_name:
        books = Book.objects.filter(title__icontains=book_name)
    elif category:
        books = Book.objects.filter(category__in=category)
    else:
        books = Book.objects.all()



    paginator = Paginator(books, 3)
    try:

        page_number = request.GET.get('page')

        books = paginator.get_page(page_number)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)




    categories = Category.objects.all()
    book_by_genres = {}


    for category in categories:
        genre = category.genre
        if genre not in book_by_genres:
            book_by_genres[genre] = []
        book_by_genres[genre].append(category)

    print(book_by_genres)

    return render(request, 'index.html', {'books': books, 'book_by_genres': book_by_genres})




def detail(request, pk):
    book = Book.objects.get(pk=pk)

    related_books = Book.objects.filter(category__in=book.category.all()).exclude(id=book.id)
    return render(request, 'detail.html', {'book': book, 'related_books': related_books})


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()
        return redirect('bookshop:index')

    else:
        form = BookForm()
        return render(request, 'add_book.html', {'form': form})