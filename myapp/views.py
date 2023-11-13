from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User


import requests
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def AboutUs(request):
    return render(request,'about-us.html')

def TopCoins(request):
    return render(request,'Top-coins.html')

def signup(request):

    
    return render(request,'signup')

def LoginUser(request):
    if request.method == "POST" :
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, "Logged Successfully!")
            return redirect("/")
    
        else:
            messages.success(request, "Please Enter Valid Password And Unsername!")
            return render(request,'login-page.html')
    return render(request,'login-page.html')

def LogOut(request):
     logout(request)
     return render(request,'login-page.html')



def btc_price(request):
    api_url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
    response = requests.get(api_url)
    data = response.json()
    btc_price = data['bitcoin']['usd']

    return render(request, 'Top-coins.html', {'btc_price':btc_price})


def signupuser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        rpassword = request.POST['password']

        myuser = User.objects.create(username,email,password,password)
        myuser.username=username
        myuser.email=email

        myuser.save()

        messages.success(request,"Your account as been successfully created .")

 
    
    return render(request,'signupuser.html')
    