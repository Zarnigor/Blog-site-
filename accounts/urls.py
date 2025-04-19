from django.contrib.auth.views import LogoutView
from django.urls import path
from accounts.views import signup, signin, profile_page

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('logout/', LogoutView.as_view(next_page='signin'), name='logout'),
    path('profile/', profile_page, name='profile_page')
]