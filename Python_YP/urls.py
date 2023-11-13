"""
URL configuration for Python_YP project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from myapp import views

admin.site.site_header = "Techie Yp Admin "
admin.site.site_title = "Techie Yp admin  "
admin.site.index_title = "Welcome to Techie Yp   "


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='home'),
    path('AboutUs',views.AboutUs,name='AboutUs'),
    path('TopCoins',views.TopCoins,name='TopCoins'),
    path('LoginUser',views.LoginUser,name='LoginUser'),
    path('LogOut',views.LogOut,name='LogOut'),
    path('btc_price', views.btc_price, name='btc_price'),
    path('signupuser', views.signupuser, name='signupuser'),
     
 
 ]
