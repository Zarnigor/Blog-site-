from django.contrib.auth.models import User
from django.db.models import Model, CASCADE, ForeignKey, DateTimeField, CharField, TextField


class Comment(Model):
    title = CharField(max_length=200)
    author = ForeignKey(User, on_delete=CASCADE)
    created_at = DateTimeField(auto_now_add=True)
    content = TextField()
