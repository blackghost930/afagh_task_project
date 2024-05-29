from rest_framework import serializers

from .models import Author, Book


class AuthorSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'price', 'author']

    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length=255)
    # price = serializers.IntegerField()
    author = serializers.HyperlinkedRelatedField(
        queryset=Author.objects.all(),
        view_name='author_detail',
    )

    def create(self, validated_data):
        book = Book(**validated_data)
        book.status = 'drf'
        book.save()
        return book



