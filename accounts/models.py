from django.contrib.auth.models import User
from django.db.models import Model, TextField, CASCADE, DateTimeField, ImageField, OneToOneField, IntegerField, CharField


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    bio = TextField()
    age = IntegerField()
    location = CharField(max_length=255)
    profile_picture = ImageField(upload_to="profile_pictures/", null=True, blank=True)
    joined_date = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} Profile"