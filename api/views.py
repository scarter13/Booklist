from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Book, Author, Note
from .serializers import BookSerializer,  AuthorSerializer, NoteSerializer
from django_filters import rest_framework as filters


class BookFilter(filters.FilterSet):
    class Meta:
        model = Book
        fields = ['status']

class BookViewSet(viewsets.ModelViewSet):
    #queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_class = BookFilter


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = Book.objects.filter(user=self.request.user)
        return queryset



class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

