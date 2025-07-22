from rest_framework.generics import ListCreateAPIView
from .models import Comment
from .serializers import CommentSerializer

class CommentListCreateAPIView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer