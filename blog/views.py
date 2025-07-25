from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Comment, Post
from .serializers import CommentSerializer, PostSerializer
from .permissions import IsOwnerOrReadOnly


class CommentListCreateAPIView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostViewSet(ViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(authod=self.request.user)