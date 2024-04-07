from django.urls import path, include
from rest_framework import routers
from books.views import *


router = routers.SimpleRouter()
router.register('newsfeed', NewsFeedListView, 'newsfeed')
router.register('favorites', FavoriteBooksListView, 'favorites')
router.register('books', BooksListRetrieveView, 'books')
router.register('comment', CommentCreateDestroyView, 'comment')

urlpatterns = [
    path('', include(router.urls)),
]
