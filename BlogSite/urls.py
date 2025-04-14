from django.contrib import admin
from django.urls import path, include
urlpatterns = [
       path('admin/', admin.site.urls),
       path('something/', include('blog.urls')),
       path('', include('accounts.urls')),
]
