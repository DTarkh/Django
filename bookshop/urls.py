from django.urls import path
from . import views

app_name = 'bookshop'

urlpatterns = [
    path('', views.index, name='index'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:pk>/', views.detail, name='book_detail'),

]

