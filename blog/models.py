from django.contrib.auth.models import AbstractUser, User
from django.db.models import Model, CharField, TextField, ForeignKey, CASCADE, DateTimeField, ImageField, OneToOneField

from accounts.models import UserProfile


class Post(Model):
    title = CharField(max_length=200)
    content = TextField()
    author = ForeignKey(UserProfile, CASCADE)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)


class Comment(Model):
    post = ForeignKey(Post, CASCADE)
    user = ForeignKey(UserProfile, CASCADE)
    content = TextField()
    created_at = DateTimeField(auto_now_add=True)



