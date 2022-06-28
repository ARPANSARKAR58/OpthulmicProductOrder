import email
from email import message
import random
from string import digits
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, renderer_classes
from .models import *
from .forms import CreateUserForm
#from .forms import RegistrationForm
#from .serializers import accountserializer
from .decorators import *
from django.contrib import messages
from rest_framework.response import Response
from rest_framework import status

from django.core.mail import send_mail
import math,random
from . import Defaults
from . import DB_Transactions
from .models import OrderRegistration
from . import Defaults
from . import DBUtils

import random
import string
import pyodbc


# Create your views here.
@csrf_exempt
def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(6):
        OTP +=digits[math.floor(random.random()*10)]
    return OTP

@csrf_exempt
def send_otp(request):
    email = request.POST.get("email")
    print("email",email)
    o=generateOTP()
    print(o)
    htmlgen = '<p>Your otp is <strong>'+o+'</strong></p>'
    send_mail('OTP request',o,'<gmail id>',[email],fail_silently=False,html_message=htmlgen)
    print(o)
    res = HttpResponse(o)
    print(res.status_code)
    print(type(res.status_code))
    if res.status_code == 200:
        print("if condition")
        jso= {"status":"Success","result":{"OTP":o}}
        return JsonResponse(jso)
    else:
        jso= {"status":"Error","result":"provide valid emailid"}
        return JsonResponse(jso)
def otpPage(request):
    return render(request, 'FDA/varifyOtp.html')






def starting(request):
    return render(request, 'FDA/start.html')

# @unauthenticated_user
@login_required(login_url='login')
def home(request):
    return render(request, 'FDA/index.html')


@csrf_exempt
def RegisterPage(request):
    
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.instance.username = form.instance.email
            name = form.instance.username
            out = username_exists(name)
            if out is False:
                user = form.save()
                # print(user)
                username = form.cleaned_data.get('email')
                group = Group.objects.get(name='customer')
                user.groups.add(group)
                # messages.success(request, 'account was created for ' + username)
                res = {"status":"Success","result":{"responce":"account was created for "+username}}
                return JsonResponse(res)
            # return redirect('login')
            else:
                res = {"status":"Error","result":{"responce":"User is Already exists"}}
                return JsonResponse(res)
        else:
            res = {"status":"Error","result":{"responce":"need to re enter in the form"}}
            return JsonResponse(res)
    context = {'form':form}
    return render(request, 'FDA/register.html',context)

# @csrf_exempt
# @unauthenticated_user
def loginpage(request):
    # if request.user.is_authenticate:
    #     return redirect('dashboard/')
    # else:
    if request.method == 'POST':
        Username = request.POST.get('username')
        Password = request.POST.get('password')

        user = authenticate(request, username=Username,password=Password)
        if user is not None:
            login(request,user)
            # return redirect('dashboard')
            res = {"status":"Success","result":{"responce":"login successfull"}}
            return JsonResponse(res)
        else:
            # messages.info(request,'Username Or Password is Incurrect')
            res = {"status":"Error","result":{"responce":"Username Or Password is Incurrect"}}
            return JsonResponse(res)
    context= {}
    return render(request, 'FDA/login.html',context)


@api_view(['POST'])
# @login_required(login_url='login')
# @allowed_users(allowed_roles=['customer'])
def loginpage_withCustCode(request):
    # if request.user.is_authenticate:
    #     return redirect('dashboard/')
    # else:
    if request.method == 'POST':
        custcode = request.data.get('custcode')
        print(custcode)
        Password = request.data.get('password')

        # user = authenticate(request, username=Username,password=Password)
        user_cust = Customer.objects.get(custcode=custcode)
        username = user_cust.mobile_phone
        # username = Customer.objects.get()
        user = authenticate(request, username=Username,password=Password)
        print("hhhh",user)
        if user is not None:
            login(request,user)
            # return redirect('dashboard')
            res = {"status":"Success","result":{"responce":"login successfull"}}
            return JsonResponse(res)
        else:
            # messages.info(request,'Username Or Password is Incurrect')
            res = {"status":"Error","result":{"responce":"Username Or Password is Incurrect"}}
            return JsonResponse(res)
    context= {}
    return render(request, 'FDA/login.html',context)



def logoutUser(request):
    logout(request)
    return redirect('login')

def username_exists(username):
    # print("into new function")
    if User.objects.filter(username=username).exists():
        return True
    
    return False

@api_view(['POST'])
# @csrf_exempt
def Find_distance(request):
    lat = DB_Transactions.get_latutide()
    lon = DB_Transactions.get_longitute()
    print(latitude)
    print(longitute)
    latitude = list(lat)
    longitude = list(lon)
    print(latitude)
    print(longitute)



# @api_view(['POST'])
# #@csrf_exempt
# def OrderRegistrationPage(request):
#         if request.method == 'POST':
#             user = request.data.get("invoiceId")
#             invoiceId = request.data.get("invoiceId")
#             invoiceId = request.data.get("invoiceId")
#             invoiceId = request.data.get("invoiceId")
#             invoiceId = request.data.get("invoiceId")
#             invoiceId = request.data.get("invoiceId")
#             invoiceId = request.data.get("invoiceId")
#             invoiceId = request.data.get("invoiceId")
#             invoiceId = request.data.get("invoiceId")
        

    
@api_view(['GET'])
#@csrf_exempt
def Marketing(request):
    
    if request.method == 'GET':
        
        
        #context = {'form':form}
        res = {"status":"Success","result":{"responce":"success"}}
    return False


# @api_view(['POST'])
# @csrf_exempt
# def Sales_data(request):
    
#     if request.method == 'POST':
#         if request.POST.get('invoiceId') and request.POST.get('invoiceDate') and request.POST.get('customerId') and request.POST.get('tsds') and request.POST.get('lensIndex') and request.POST.get('lensFocality') and request.POST.get('prodBrand') and request.POST.get('prodSubBrand') and request.POST.get('itemGroupId') and request.POST.get('lensSold') and request.POST.get('coating') and request.POST.get('soldQuantity') and request.POST.get('lensSoldValue') and request.POST.get('discount') and request.POST.get('lensNetSaleValue'):
#             saverecord=Sales
#             saverecord.invoiceId=request.POST.get('invoiceId')
#             saverecord.invoiceDate=request.POST.get('invoiceDate')
#             saverecord.customerId=request.POST.get('customerId')
#             saverecord.tsds=request.POST.get('tsds')
#             saverecord.lensIndex=request.POST.get('lensIndex')
#             saverecord.lensFocality=request.POST.get('lensFocality')
#             saverecord.prodBrand=request.POST.get('prodBrand')
#             saverecord.prodSubBrand=request.POST.get('prodSubBrand')
#             saverecord.itemGroupId=request.POST.get('itemGroupId')
#             saverecord.lensSold=request.POST.get('lensSold')
#             saverecord.coating=request.POST.get('coating')
#             saverecord.soldQuantity=request.POST.get('soldQuantity')
#             saverecord.lensSoldValue=request.POST.get('lensSoldValue')
#             saverecord.discount=request.POST.get('discount')
#             saverecord.lensNetSaleValue=request.POST.get('lensNetSaleValue')
#             saverecord.save()
#             messages.success(request,'Getting Data Successfully.......')
#             res = {"status":"Success","result":{"responce":"success"}}
#             return render(request, 'given.html',context)
#     else:
#         return render(request, 'given.html',context)
#         #context = {'form':form}
#         res = {"status":"Success","result":{"responce":"success"}}
#     return False

@api_view(['POST'])
#@csrf_exempt
def Sales_Insurt(request):
    if request.method == 'POST':
        invoiceId = request.data.get("invoiceId")
        invoiceDate = request.data.get("invoiceDate"+5.30)
        customerId = request.data.get("customerId ")
        tsds = request.data.get("tsds")
        lensIndex = request.data.get("lensIndex")
        lensFocality = request.data.get("lensFocality")
        prodBrand = request.data.get("prodBrand")
        prodSubBrand = request.data.get("prodSubBrand")
        itemGroupId = request.data.get("itemGroupId")
        lensSold = request.data.get("lensSold")
        coating = request.data.get("coating")
        soldQuantity = request.data.get("soldQuantity")
        lensSoldValue = request.data.get("lensSoldValue")
        discount = request.data.get("discount")
        lensNetSaleValue = request.data.get("lensNetSaleValue")
        insurt_sales_data = Sales(invoiceId=str(invoiceId),invoiceDate=float(invoiceDate),customerId=str(customerId),tsds=str(tsds),lensIndex=(lensIndex),lensFocality=str(lensFocality),prodBrand=str(prodBrand),prodSubBrand=str(prodSubBrand),itemGroupId=str(itemGroupId),lensSold=str(lensSold),coating=str(coating),soldQuantity=str(soldQuantity),lensSoldValue=str(lensSoldValue),)
        insurt_sales_data.save()
        return JsonResponse({"status":"success"})
    return JsonResponse({"status":"fail"})



@api_view(['GET'])
#@csrf_exempt
def iamherenow(request):
    return render(request, 'FDA/start.html')



@api_view(['GET'])
#@csrf_exempt
def databaseconnect(request):
    db = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+Defaults.host_ms+';DATABASE='+Defaults.schema_ms+';UID='+Defaults.user_ms+';PWD='+ Defaults.password_ms)
    
    if pyodbc.connect == True:
        print("Connection done...")
        return render(request, 'FDA/index.html')
    else:
        print("Connection failed...")
        return render(request, 'FDA/connection.html')
    

@api_view(['GET'])
@login_required(login_url='login')
def Get_all_orders(request):
    items  = []
    resp = DB_Transactions.get_all_orders()
    for row in resp:
        items.append({'castomer_code': row[0], 'application_name': row[1], 'country' : row[2], 'email' : row[3], 'mobile_phone' : row[4]})
    disc = {"status": "Success", "result":{"Node":items}}
    return Response(disc )


# @api_view(['POST'])
# #@csrf_exempt
# def new_customer_entry(request):
#     if request.method == 'POST':
#         invoiceId = request.data.get("invoiceId")
#         invoiceDate = request.data.get("invoiceDate")
#         customerId = request.data.get("customerId ")
#         tsds = request.data.get("tsds")
#         lensIndex = request.data.get("lensIndex")
#         lensFocality = request.data.get("lensFocality")
#         prodBrand = request.data.get("prodBrand")
#         prodSubBrand = request.data.get("prodSubBrand")
#         itemGroupId = request.data.get("itemGroupId")
#         lensSold = request.data.get("lensSold")
#         coating = request.data.get("coating")
#         soldQuantity = request.data.get("soldQuantity")
#         lensSoldValue = request.data.get("lensSoldValue")
#         discount = request.data.get("discount")
#         lensNetSaleValue = request.data.get("lensNetSaleValue")
#         insurt_sales_data = Sales(invoiceId=str(invoiceId),invoiceDate=str(invoiceDate),customerId=str(customerId),tsds=str(tsds),lensIndex=(lensIndex),lensFocality=str(lensFocality),prodBrand=str(prodBrand),prodSubBrand=str(prodSubBrand),itemGroupId=str(itemGroupId),lensSold=str(lensSold),coating=str(coating),soldQuantity=str(soldQuantity),lensSoldValue=str(lensSoldValue),)
#         insurt_sales_data.save()
#         return JsonResponse({"status":"success"})
#     return JsonResponse({"status":"fail"})