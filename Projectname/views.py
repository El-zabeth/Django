from django.shortcuts import render

from django.views.decorators.cache import never_cache
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt

@never_cache
def register_page(request):
    return render(request,'register.html')

@never_cache
def login_page(request):
    return render(request,'login.html')

@never_cache
@csrf_exempt
def register(request):
    name = request.POST.get('name')
    email = request.POST.get('mail')
    password = request.POST.get('password')
    password2 = request.POST.get('password2')
    phone = request.POST.get('phone')
    data={}
    print(f'Name: {name}, Mail: {email}, Password: {password}, Phone: {phone}')
    reg_ob=User(name=name,email=email,password=password,phone=phone)
    reg_ob.save()
    data['result']='yes'
    return JsonResponse(data,safe=False)
