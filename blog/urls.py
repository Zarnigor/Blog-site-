from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommentListCreateAPIView, PostViewSet

router = DefaultRouter()
router.register(r'post', PostViewSet, basename='post')


urlpatterns = [
    path('comments/', CommentListCreateAPIView.as_view()),
    path('', include('router.urls'))
]
