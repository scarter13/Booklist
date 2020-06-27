from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Book, Author, Note
#from api.serializers import UserSerializer, BookSerializer,  AuthorSerializer, NoteSerializer,

# Create your views here.

#class UserViewSet(viewsets.ModelViewSet):
    #queryset = User.objects.all()
    #serializer_class = UserSerializer
    #permission_classes =[permissions.IsAuthenticated]