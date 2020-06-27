from rest_framework import serializers
from .models import Book, Author, Note

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields =[
            'book',
            'last_name',
            'first_name',
        ]

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields =[
            'book',
            'text',
            'date',
            'page',
        ]

class BookSerializer(serializers.HyperlinkedModelSerializer):
    authors = AuthorSerializer(many=True, required=False)
    notes = NoteSerializer(many=True, required=False)
    class Meta:
        model = Book
        fields =[
            'url',
            'user',
            'title',
            'status',
            'authors',
            'notes',
        ]
