import datetime
import hashlib
import json
from collections import Counter

import torch
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from django.db.models import Sum, Count, Max, Min, Avg
from django.contrib import auth
from django.contrib.auth.hashers import make_password, check_password
import django.contrib.auth.models as auth_models
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from myapp.forecast import Net, predict
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
        return render(request, "login.html")
    username = request.POST.get("userName")
    password = request.POST.get("userPassword")
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        return HttpResponse({"success": False, "message": "用户名已存在"})
    auth_models.User.objects.create_user(username=username, password=password)
    return HttpResponse({"success": True, "message": "注册成功"})
