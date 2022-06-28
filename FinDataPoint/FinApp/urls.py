from django.urls import path
from . import views

urlpatterns = [
    path('', views.starting),
    path('dashboard/', views.home, name="dashboard"),
    path('register/', views.RegisterPage, name="registration"),
    path('login/', views.loginpage, name="login"),
    path('login_custcode/', views.loginpage_withCustCode, name="loginWithCode"),
    path('logout/', views.logoutUser, name="logout"),
    path('send_otp/', views.send_otp, name="send otp"),
    path('otp_page/', views.otpPage, name="otp"),
    path('otp_page/register', views.RegisterPage, name="otp"),
    #path('OrderRegistration/', views.OrderRegistrationPage, name="OrderRegistration"),
    #path('accounts/', views.accounts, name="accounts"),
    path('Marketing/', views.Marketing, name="Maketing"),
    path('Sales/', views.Sales_Insurt, name="Sales"),
    path('mypresence/', views.iamherenow, name="mypresence"),
    path('dbconnect/', views.databaseconnect, name="dbconnect"),
]