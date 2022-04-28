from datetime import timezone

from django.contrib import auth
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from myapp.models import *
import myapp.verification as verification
import logging

logger = logging.getLogger(__name__)


@csrf_exempt
def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    username = request.POST.get("userName")
    password = request.POST.get("userPassword")
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return JsonResponse({"success": True, "message": "登录成功"})
    return JsonResponse({"success": False, "message": "用户名或密码错误"})


@csrf_exempt
def register(request):
    if request.method == "GET":
        return render(request, "register.html")
    username = request.POST.get("userName")
    password = request.POST.get("userPassword")
    user = User.objects.create_user(username=username, password=password)
    if user is not None:
        user.is_active = False
        return JsonResponse({"success": True, "message": "注册成功"})
    return JsonResponse({"success": False, "message": "用户名已存在"})


@csrf_exempt
def logout(request):
    auth.logout(request)
    return JsonResponse({"success": True, "message": "注销成功"})


def set_pet_info(request):
    if request.method == "GET":
        return render(request, "set_pet_info.html")
    new_pet = Pet()
    new_pet.pet_name = request.POST.get("petName")
    new_pet.pet_type = request.POST.get("petType")
    new_pet.pet_breed = request.POST.get("petBreed")
    new_pet.pet_gender = request.POST.get("petGender")
    new_pet.pet_date_of_birth = request.POST.get("petDateOfBirth")
    new_pet.save()
    user_id = request.session.get('_auth_user_id')
    user = User.objects.get(id=user_id)
    user.pet = new_pet
    user.save()
    return JsonResponse({"success": True, "message": "宠物信息设置成功"})


def get_pet_info(request):
    user_id = request.session.get('_auth_user_id')
    user = User.objects.get(id=user_id)
    pet = user.pet
    pet_info = {
        "petName": pet.pet_name,
        "petType": pet.pet_type,
        "petBreed": pet.pet_breed,
        "petGender": pet.pet_gender,
        "petAge": (datetime.now(timezone.utc) - pet.pet_date_of_birth).days
    }
    return JsonResponse(pet_info)


def get_verification_code(request):
    user_id = request.session.get('_auth_user_id')
    user = User.objects.get(id=user_id)
    verification.send_code(user.email)
    return JsonResponse({"success": True, "message": "验证码已发送"})


def verify_code(request):
    user_id = request.session.get('_auth_user_id')
    user = User.objects.get(id=user_id)
    code = request.POST.get("code")
    records = EmailVerificationCode.objects.filter(code=code)
    for record in records:
        if record.user.id == user.id:
            user.is_active = True
            user.save()
            record.delete()
            return JsonResponse({"success": True, "message": "验证码正确"})
    return JsonResponse({"success": False, "message": "验证码错误"})
