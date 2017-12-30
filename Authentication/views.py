from django.shortcuts import render, redirect
from .models import User


def index(request):
    if request.session.has_key('username'):
        one_entry = User.objects.get(user_email=request.session['username'])
        # print(one_entry.user_email)

        if one_entry.user_role == '1':
            return redirect('/administrator/dashboard')
        elif one_entry.user_role == '2':
            return redirect('/bde/dashboard')
    else:
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
            request.session['username'] = username
            request.session['name'] = one_entry.user_name
            if one_entry.user_role == '1':
                return redirect('/administrator/dashboard')
            elif one_entry.user_role == '2':
                return redirect('/bde/dashboard')
        except User.DoesNotExist:
            print("No user found.")
            return render(request, "Authentication/login.html", context={"error": 'Wrong username or password.'})


