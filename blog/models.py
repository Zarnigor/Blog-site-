from django.contrib.auth.models import AbstractUser, User
from django.db.models import Model, CharField, TextField, ForeignKey, CASCADE, DateTimeField, ImageField, OneToOneField
from accounts.models import Profile


class Category(Model):
    title = CharField(max_length=200)

class Post(Model):
    title = CharField(max_length=200)
    content = TextField()
    author = ForeignKey(Profile, CASCADE)
    category = ForeignKey(Category, CASCADE)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

        
class Comment(Model):
    post = ForeignKey(Post, CASCADE)
    user = ForeignKey(Profile, CASCADE)
    content = TextField()
    created_at = DateTimeField(auto_now_add=True)



