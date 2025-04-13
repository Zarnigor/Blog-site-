from django.shortcuts import render

def posts(request):
    return render(request, 'blog/index.html', )

def about(request):
    return render(request, 'blog/about.html')

def post(request):
    return render(request, 'blog/post.html')

def contact(request):
    return render(request, 'blog/contact.html')