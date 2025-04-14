from django.urls import path
from accounts.views import signup, signin

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
]