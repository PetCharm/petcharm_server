from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render

from myapp.models import *
import logging

logger = logging.getLogger(__name__)


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    username = request.POST.get("userName")
    password = request.POST.get("userPassword")
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponse({"success": True, "message": "登录成功"})
    return HttpResponse({"success": False, "message": "用户名或密码错误"})


def register(request):
    if request.method == "GET":
        return render(request, "register.html")
    username = request.POST.get("userName")
    password = request.POST.get("userPassword")
    user = User.objects.create_user(username=username, password=password)
    if user is not None:
        return HttpResponse({"success": True, "message": "注册成功"})
    return HttpResponse({"success": False, "message": "用户名已存在"})
