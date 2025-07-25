from django.contrib.auth.models import User
from django.db.models import Model, CASCADE, ForeignKey, DateTimeField, CharField, TextField, BooleanField, ImageField, SlugField


class Post(Model):
    title = CharField(max_length=200)
    slug = SlugField(unique=True)
    author = ForeignKey(User, on_delete=CASCADE, related_name='Posts')
    content = TextField()
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    is_published = BooleanField(default=True)
    image = ImageField(upload_to='images/', null=True, blank=True)

class Comment(Model):
    title = CharField(max_length=200)
    author = ForeignKey(User, on_delete=CASCADE, related_name='Comments')
    created_at = DateTimeField(auto_now_add=True)
    content = TextField()
    post = ForeignKey(Post, on_delete=CASCADE)

