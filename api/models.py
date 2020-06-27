from django.db import models
#from users.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class User(AbstractUser):
    pass

class Book(models.Model):
    NOT_READ = 'NTRD'
    READING = 'RDNG'
    READ = 'READ'
    STATUS_CHOICES =[
        (NOT_READ, 'Not Yet Read'),
        (READING, 'Currently Reading'),
        (READ, 'Finished Reading'),
    ]
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, related_name='books')
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=4, choices=STATUS_CHOICES, default=NOT_READ)

    
class Note(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, related_name='notes')
    book = models.ForeignKey(to = Book, on_delete = models.CASCADE, related_name='notes')
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    page = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.text


class Author(models.Model):
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE, null=True, blank=True, related_name='books')
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"
