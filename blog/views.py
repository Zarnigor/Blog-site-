from django.shortcuts import render

def posts(request):
    return render(request, 'index.html', )

def about(request):
    return render(request, 'about.html')

def post(request):
    return render(request, 'post.html')

def contact(request):
    return render(request, 'contact.html')