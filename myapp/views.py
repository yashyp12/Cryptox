from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from .forms import ContactForm
from django.http import JsonResponse


import requests
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def AboutUs(request):
    return render(request,'about-us.html')

def TopCoins(request):
    return render(request,'Top-coins.html')

 
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
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_repeat = request.POST.get('password_repeat')

        # Check if passwords match
        if password != password_repeat:
            messages.error(request, "Passwords do not match.")
            return redirect('signupuser')  # You may need to adjust the URL name if it's different

        # Create a new user
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, "Your account has been successfully created.")
            return redirect('home')  # You may need to adjust the URL name if it's different
        except Exception as e:
            messages.error(request, f"Error creating user: {str(e)}")
            return redirect('signupuser')  # You may need to adjust the URL name if it's different

    return render(request, 'signupuser.html')

def aboutus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been submitted successfully.")
            return redirect('AboutUs')  # Redirect to the About Us page or any other page you prefer
        else:
            messages.error(request, "Please correct the errors in the form.")
    else:
        form = ContactForm()

    return render(request, 'about-us.html', {'form': form})