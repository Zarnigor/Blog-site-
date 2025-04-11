from django.contrib.auth.models import User
from django.db.models import Model, TextField, CASCADE, DateTimeField, ImageField, OneToOneField


class UserProfile(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    bio = TextField()
    profile_picture = ImageField(upload_to="profile_pictures/", null=True, blank=True)
    joined_date = DateTimeField(auto_now_add=True)
