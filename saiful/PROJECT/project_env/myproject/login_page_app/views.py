from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.

def login(request):
    
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
           
            auth.login(request, user)
            return redirect('/home_page')
        else:
            print('invalid credentials')
            messages.info(request, 'invalid credentials')
            return redirect('login')

    else:
        print('Go to login page')
        return render(request, 'login_page_app/login_page.html')