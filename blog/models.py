from django.db.models import Model, CharField, TextField, ForeignKey, CASCADE, DateTimeField


class UserProfile(Model):
    pass


class Category(Model):
    title = CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"


class Post(Model):
    title = CharField(max_length=200)
    content = TextField()
    author = ForeignKey(UserProfile, CASCADE)
    category = ForeignKey(Category, CASCADE)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)


class Comment(Model):
    post = ForeignKey(Post, CASCADE)
    user = ForeignKey(UserProfile, CASCADE)
    content = TextField()
    created_at = DateTimeField(auto_now_add=True)



