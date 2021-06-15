from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def sign_in(request):
    if request.method == "GET":
       return render(request, 'account_app/login.html') 
    
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return render(request, 'index.html')
            
        elif user is None:
            return render(request, 'account_app/login.html')

def sign_out(request):
    logout(request)
    return render(request, 'index.html')

def register(request):
    if request.method == 'GET':
        return render(request, 'account_app/register.html')
    
    elif request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['pasword']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            pass
        else:
            user = User.objects.create_user(first_name= first_name, last_name = last_name, username = username, email = email, password = password)
            user.save()      
            return render(request, 'account_app/login.html')
        