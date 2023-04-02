from django.urls import path
from .views import BookListView, BookDetailView, AuthorListView, AuthorDetailView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', BookListView.as_view(), name='books'),
    path('book/<int:pk>', BookDetailView.as_view(), name='book-detail'),
    path('author/<int:pk>', AuthorDetailView.as_view(), name='author-detail'),
    path('authors/', AuthorListView.as_view(), name='author'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('book/<int:pk>/renew/', views.renew_book_librarian, name='renew_book_librarian'),
    path('borrowed/', views.LoanedBooksAllListView.as_view(), name='all-borrowed'),
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
]
