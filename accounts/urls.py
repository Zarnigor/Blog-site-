from django.contrib.auth.views import LogoutView
from django.urls import path
from accounts.views import signup, signin

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('logout/', LogoutView.as_view(next_page='signin'), name='logout'),
]