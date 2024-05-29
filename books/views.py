from django.shortcuts import render
from django.views import generic

from .models import Book, Author


class DynamicPage:
    book_des = {
        'model': Book,
        'template_name': 'books/book_list.html',
        'context_object_name': 'book'
    }


class BookListView(generic.ListView):
    book_dict = DynamicPage.book_des

