from rest_framework.serializers import ModelSerializer, ReadOnlyField
from .models import Comment, Post

class CommentSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        exclude = ['id']

class PostSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        exclude = ['Post']