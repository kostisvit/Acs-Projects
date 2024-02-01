from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect

from .models import CustomUser
from django.contrib.auth import logout

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        if email and password:
            user = authenticate(request, email=email, password=password)

            if user is not None:
                auth_login(request, user)
                
                return redirect('/')

    return render(request, 'account/login.html')




def logout_request(request):
  logout(request)
  #messages.info(request, "Logged out successfully!")
  return redirect("/")