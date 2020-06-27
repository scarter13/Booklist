from rest_framework import serializers
from core.models import Book, Author, Note

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields =[
            'book',
            'last_name',
            'first_name',

        ]

class BookSerializer(serializers.HyperlinkedModelSerializer):
    authors = AuthorSerializer(many=True, required=False)
    class Meta:
        model = Book
        fields =[
            'url',
            'user',
            'title',
            'status',
            'authors',
        ]
"""
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, related_name='books')
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=4, choices=STATUS_CHOICES, default=NOT_READ)
"""