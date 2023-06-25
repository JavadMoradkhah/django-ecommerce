from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib import messages
from . import forms

User = get_user_model()


def signup_user(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'auth/signup.html', {'form': forms.SignUpForm()})
    elif request.method == 'POST':
        form = forms.SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            # username = request.POST.get('username')
            # email = request.POST.get('email')
            # password = request.POST.get('password1')
            # user = User.objects.create_user(username, email, password)
            # login_user(request, user)
            return redirect('/')
        else:
            return render(request, 'auth/signup.html', {'form': form})


def login_user(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST.get('username'),
        password = request.POST.get('password')

        user = authenticate(
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(
                request,
                'Please enter a correct username and password'
            )
            return render(request, 'auth/login.html')
    else:
        return render(request, 'auth/login.html', {'form': None})
