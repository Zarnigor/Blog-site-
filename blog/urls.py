from blog.views import posts, about, post, contact
from django.urls import path


urlpatterns = [
    path('', posts, name='index'),
    path('about/', about, name='about'),
    path('post-detail/', post, name='post-detail'),
    path('contact/', contact, name='contact'),
]