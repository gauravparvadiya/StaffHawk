from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import User
from django.urls import reverse


def index(request):
    return render(request, "Authentication/login.html")


def login(request):

    if request.method == 'POST':
        print('Got the request!!!')
        print(request.POST['username'])
        print(request.POST['password'])
        username = request.POST['username']
        password = request.POST['password']
        try:
            one_entry = User.objects.get(user_email=username,user_password=password)
            print('User found')
            return redirect('/administrator/dashboard')
        except User.DoesNotExist:
            print("No user found.")
            return render(request, "Authentication/login.html", context={"error": 'Wrong username or password.'})


