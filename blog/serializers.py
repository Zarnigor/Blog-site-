from rest_framework.serializers import ModelSerializer
from .models import Comment, Post

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        exclude = ['id']

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        exclude = ['Post']