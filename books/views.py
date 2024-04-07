from rest_framework import mixins, status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.filters import  SearchFilter

from books.models import Book, UserBook, Comment
from books.serializers import (NewsFeedSerializer,
                               FavoritesListSerializer,
                               CommentSerializer,
                               AddCommentSerializer,
                               BookSerializer)
from django.shortcuts import get_object_or_404


class NewsFeedListView(viewsets.GenericViewSet,
                       mixins.ListModelMixin):
    """
    Лента о поступлении новых книг
    """

    queryset = Book.objects.all().order_by('-created_at')
    serializer_class = NewsFeedSerializer


class BooksListRetrieveView(viewsets.GenericViewSet,
                            mixins.ListModelMixin,
                            mixins.RetrieveModelMixin):

    """
    Список книг, просмотр конкретных книг и комментарии к ним
    """

    queryset = Book.objects.all()
    serializer_class = FavoritesListSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name',)


    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = Book.objects.all()
        obj = get_object_or_404(queryset, pk=self.kwargs.get('pk'))
        serializer = BookSerializer(obj)
        return Response(serializer.data)


class FavoriteBooksListView(viewsets.GenericViewSet,
                            mixins.ListModelMixin,
                            mixins.RetrieveModelMixin):

    """Список книг добавленных в избранные"""

    queryset = Book.objects.all()
    serializer_class = FavoritesListSerializer
    permission_classes = [IsAuthenticated,]

    def list(self, request, *args, **kwargs):
        queryset = (Book.objects.filter(user_book__user=request.user, user_book__favorites=True))
        serializer = FavoritesListSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_object(self):
        queryset = Book.objects.all()
        pk = self.kwargs.get('pk')
        obj = get_object_or_404(queryset, pk=pk)
        return obj


    def retrieve(self, request, *args, **kwargs):

        """
        Передаем id книги во входные данные!
        Если текущий пользователь и книга с переданным id
        НЕ связаны через промежуточную сущность, то создаем ее,
        а иначе удаляем.
        """

        book = self.get_object()
        obj = UserBook.objects.filter(user=request.user, book=book)
        if not obj:
            UserBook.objects.create(user=request.user, book=book, favorites=True)
            return Response(status=status.HTTP_200_OK)
        elif obj:
            UserBook.objects.get(user=request.user, book=book).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status.HTTP_404_NOT_FOUND)


class CommentCreateDestroyView(viewsets.GenericViewSet,
                               mixins.CreateModelMixin,
                               mixins.DestroyModelMixin):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [AllowAny, ]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCommentSerializer

    def get_object(self):
        queryset = Comment.objects.all()
        pk = self.kwargs.get('pk')
        obj = get_object_or_404(queryset, pk=pk)
        return obj

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
