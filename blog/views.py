from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ViewSet

from .models import Comment, Post
from .serializers import CommentSerializer, PostSerializer


class CommentListCreateAPIView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class PostViewSet(ViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer