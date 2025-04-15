from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def signin(request):
    if request.method == "POST":
        username = request.POST.get('your_name')
        password = request.POST.get('your_pass')

        if not all ([username, password]):
            messages.error(request, 'Fill the all gaps')
            return redirect('signin')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Please register first')
            return redirect('signup')

    return render(request, 'accounts/signin.html')



def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        re_pass = request.POST.get('re_pass')
        agree = request.POST.get('agree-term')

        if not all([name, email, password, re_pass, agree]):
            messages.error(request, "Please, fill the all gaps")
            return redirect('signup')

        if password != re_pass:
            messages.error(request, "Passwords doesn't match")
            return redirect('signup')

        if User.objects.filter(username=name).exists():
            messages.error(request, "Username exists")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already used")
            return redirect('signup')

        user = User.objects.create(
            username=name,
            email=email,
            password=make_password(password)
        )

        messages.success(request, "You successfully registered")
        return render(request, 'accounts/signin.html')

    return render(request, 'accounts/signup.html')

