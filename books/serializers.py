from rest_framework import serializers

from books.models import Book, Comment


class NewsFeedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['id', 'name', 'created_at']


class FavoritesListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['name']


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['content', ]


class AddCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['book', 'content']


class BookSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(many=True)

    class Meta:
        model = Book
        fields = ['name', 'comments']
