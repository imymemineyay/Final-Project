from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import User
# Create your views here.



def login_view(request):
    error = None
    if request.method == "POST" :
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            print('인증 성공')
            login(request, user)
        else:
            print('인증 실패')
            error = 'Username or Password is Incorrect'
    return render(request, 'users/login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('/')

def signup_view(request):
    if request.method == "POST" :
        print(request.POST)
        name = request.POST['name']
        employee_id = request.POST['employee_id']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        
        user = User.objects.create_user(username, email, password)
        user.name = name
        user.employee_id = employee_id
        user.save()
        return redirect('users:login')
    return render(request, 'users/signup.html')