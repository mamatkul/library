from django.urls import path
from .views import BookListView, BookDetailView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', BookListView.as_view(), name='books'),
    path('book/<int:pk>', BookDetailView.as_view(), name='book-detail'),
]
