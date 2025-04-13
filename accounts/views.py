from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


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

