from django.views import generic
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from .models import Book, Author
from .paginations import DefaultPagination
from .serializers import BookSerializer, AuthorSerializer
from .filters import BookFilter

book_des = {
    'model': "Book",
    'fields': ['title', 'author', 'text', 'price', 'status'],
    'values': {
        'book1': ('AliAlavi', 'text about book1', '200000', 'published'),
        'book2': ('Ali Alavi', 'some text about book2', '150000', 'draft'),
        'book3': ('HadiKazemi', 'some text about book3', '50000', 'published')
    },
    'relations': {
        'model': "Author",
        'fields': ['first_name', 'last_name', 'date_of_birth', 'date_of_death'],
        'values': {('Ali', 'Alavi'),
                   ('Hadi', 'Kazemi')
                   }
    }
}


def home_page_view(request):
    return render(request, 'home.html')


class BookListView(ListCreateAPIView):
    serializer_class = BookSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_class = BookFilter
    search_fields = ['title']
    pagination_class = DefaultPagination
    queryset = Book.objects.all()

    def get_serializer_context(self):
        return {'request': self.request}


class BookDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.select_related('author').all()

    def delete(self, request, pk):
        book = get_object_or_404(Book.objects.select_related('author'), pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BookAddView(generic.CreateView):
    pass


class BookEditView(generic.UpdateView):
    # Update
    # author = Author.objects.get(id=1)
    # book = Book(id=4)
    # book.title = 'New cars'
    # book.price = 45000
    # book.text = 'This a book about the best new car'
    # book.status = 'pub'
    # book.author_id = 1
    # book.save()

    # book = Book.objects.get(pk=6)
    # book.title = 'new book about birds'
    # book.price = 800000
    # book.save()
    pass


class BookDeleteView(generic.DeleteView):
    # Delete
    Book.objects.filter(pk=9).delete()


@api_view()
def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    serializer = AuthorSerializer(author, context={'request': request})
    return Response(serializer.data)


