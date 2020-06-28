from rest_framework import serializers
from .models import Book, Author, Note

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields =[
            'last_name',
            'first_name',
        ]

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields =[
            'text',
            'date',
            'page',
        ]

class BookSerializer(serializers.HyperlinkedModelSerializer):
    authors = AuthorSerializer(many=True, required=False)
    notes = NoteSerializer(many=True, required=False)

    def create(self, validated_data):
        authors_data = validated_data.pop('authors', [])
        notes_data = validated_data.pop('notes', [])
        book = Book.objects.create(**validated_data)
        for author_data in authors_data:
            Author.objects.create(book=book, **author_data)
        for note_data in notes_data:
            Note.objects.create(book=book, **note_data)
        return book

    def update(self, instance, validated_data):
        book = instance
        authors_data = validated_data.pop('authors', [])
        notes_data = validated_data.pop('notes', [])        
        for key, value in validated_data.items():
            setattr(book, key, value)
        book.save()
        for note_data in notes_data:
            Note.objects.create(book=book, **note_data)
        if authors_data != []:
            book.authors.all().delete()
            for author_data in authors_data:
                Author.objects.create(book=book, **author_data)
        return book

    

    class Meta:
        model = Book
        fields =[
            'id',
            'url',
            'user',
            'title',
            'status',
            'authors',
            'notes',
        ]
