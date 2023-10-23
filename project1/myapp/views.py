from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib  import messages

# Create your views here.
def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request='POST', username='username', password='password')
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully")
            return redirect('home')
        else:
            messages.success(request, "Login Error")
            return redirect('home')
    else:
        return render(request, 'home.html', {})
    

# def loginUser(request):
#     return render(request, 'login.html', {})

def logoutUser(request):
    logout(request)
    messages.success(request, "Logout Successful")
    return redirect('home')