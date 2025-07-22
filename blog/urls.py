from django.urls import path
from .views import CommentListCreateAPIView

urlpatterns = [
    path('comments/', CommentListCreateAPIView.as_view())
]
