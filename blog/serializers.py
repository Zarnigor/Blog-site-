from rest_framework.serializers import ModelSerializer, ReadOnlyField, CharField
from .models import Comment, Post
from django.contrib.auth.models import User

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

class RegisterSerializer(ModelSerializer):
    password = CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user