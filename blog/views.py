from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def posts(request):
    return render(request, 'blog/index.html', )

@login_required
def about(request):
    return render(request, 'blog/about.html')

@login_required
def post(request):
    return render(request, 'blog/post.html')

@login_required
def contact(request):
    return render(request, 'blog/contact.html')