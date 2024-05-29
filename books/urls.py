
from django.urls import path

import books.dynamic_page
from .dynamic_page import  BookListView ,BookDetailView, BookAddView, BookEditView, BookDeleteView, home_page_view, author_detail


urlpatterns = [
    path('', home_page_view, name='home'),
    path('list/', BookListView.as_view(), name='book_list'),
    path('detail/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('<int:pk>/update/', BookEditView.as_view(), name='book_update'),
    path('<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
    path('authors/<int:pk>/', author_detail, name='author_detail'),

]

