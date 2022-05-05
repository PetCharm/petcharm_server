from datetime import timezone

from django.contrib import auth
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView

from myapp.models import *
import myapp.verification as verification
import myapp.openIM as openIM
import myapp.info as info
import logging

logger = logging.getLogger(__name__)


class UserInfo(APIView):
    @swagger_auto_schema(
        operation_summary='获取用户信息',
        response={200: 'OK'}
    )
    def get(self, request):
        user_id = request.session.get('_auth_user_id')
        user = User.objects.get(id=user_id)
        user_info = {
            "userName": user.username,
            "userFirstName": user.first_name,
            "userLastName": user.last_name,
            "userIsActive": user.is_active,
            "userType": user.user_type,
            "userEmail": user.email,
            "userIconUrl": user.user_icon_url,
        }
        return JsonResponse(user_info)

    @swagger_auto_schema(
        operation_summary='修改用户信息',
        response={200: 'OK'}
    )
    def post(self, request):
        user_id = request.session.get('_auth_user_id')
        user = User.objects.get(id=user_id)
        user.first_name = request.POST.get("userFirstName")
        user.last_name = request.POST.get("userLastName")
        user.email = request.POST.get("userEmail")
        user.set_password(request.POST.get("userPassword"))
        user.user_icon_url = request.POST.get("userIconUrl")
        user.save()
        return JsonResponse({"success": True, "message": "用户信息设置成功"})


class LoginView(APIView):
    @swagger_auto_schema(
        operation_summary='用户登录',
        response={200: 'OK'}
    )
    @csrf_exempt
    def post(self, request):
        username = request.POST.get("userName")
        password = request.POST.get("userPassword")
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return JsonResponse({"success": True, "message": "登录成功"})
        return JsonResponse({"success": False, "message": "用户名或密码错误"})


class RegisterView(APIView):
    @swagger_auto_schema(
        operation_summary='用户注册',
        response={200: 'OK'}
    )
    @csrf_exempt
    def post(self, request):
        username = request.POST.get("userName")
        password = request.POST.get("userPassword")
        email = request.POST.get("userEmail")
        user = User.objects.create_user(username=username, password=password, email=email)
        if user is not None:
            user.is_active = False
            token = openIM.register(user.username)
            auth.login(request, user)
            return JsonResponse({"success": True, "message": "注册成功", "im_token": token})
        return JsonResponse({"success": False, "message": "用户名已存在"})


class LogoutView(APIView):
    @swagger_auto_schema(
        operation_summary='用户注销',
        response={200: 'OK'}
    )
    @csrf_exempt
    def get(self, request):
        auth.logout(request)
        return JsonResponse({"success": True, "message": "注销成功"})


class PetView(APIView):
    @swagger_auto_schema(
        operation_summary='获取宠物信息',
        response={200: 'OK'}
    )
    def get(self, request):
        user_id = request.session.get('_auth_user_id')
        user = User.objects.get(id=user_id)
        pet = user.pet
        pet_info = info.get_pet_info(pet)
        return JsonResponse(pet_info)

    @swagger_auto_schema(
        operation_summary='修改宠物信息',
        response={200: 'OK'}
    )
    def post(self, request):
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


class VerificationCodeView(APIView):
    @swagger_auto_schema(
        operation_summary='获取验证码',
        response={200: 'OK'}
    )
    def get(self, request):
        user_id = request.session.get('_auth_user_id')
        user = User.objects.get(id=user_id)
        verification.send_code(user.email)
        return JsonResponse({"success": True, "message": "验证码已发送"})

    @swagger_auto_schema(
        operation_summary='验证验证码',
        response={200: 'OK'}
    )
    def post(self, request):
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


class RetrievePasswordVerificationCodeView(APIView):
    @swagger_auto_schema(
        operation_summary='获取验证码',
        response={200: 'OK'}
    )
    def post(self, request):
        username = request.POST.get("username")
        user = User.objects.get(username=username)
        if not user.is_active:
            return JsonResponse({"success": False, "message": "该用户未绑定邮箱"})
        verification.send_code(user.email)
        return JsonResponse({"success": True, "message": "验证码已发送"})


class RetrievePasswordView(APIView):
    @swagger_auto_schema(
        operation_summary='找回密码',
        response={200: 'OK'}
    )
    def post(self, request):
        username = request.POST.get("username")
        user = User.objects.get(username=username)
        code = request.POST.get("code")
        records = EmailVerificationCode.objects.filter(code=code)
        for record in records:
            if record.user == user:
                user.set_password(request.POST.get("password"))
                user.save()
                record.delete()
                return JsonResponse({"success": True, "message": "密码修改成功"})
        return JsonResponse({"success": False, "message": "验证码错误"})


class AllPostsView(APIView):
    @swagger_auto_schema(
        operation_summary='获取所有帖子',
        response={200: 'OK'}
    )
    def get(self, request):
        posts = Post.objects.all()
        posts_info = []
        for post in posts:
            post_info = {
                "postId": post.id,
                "postTitle": post.title,
                "postContent": post.content,
                "postDate": post.date
            }
            posts_info.append(post_info)
        return JsonResponse(posts_info, safe=False)


class AllCommentsView(APIView):
    @swagger_auto_schema(
        operation_summary='获取所有评论',
        response={200: 'OK'}
    )
    def get(self, request):
        post_id = request.GET.get("postId")
        post = Post.objects.get(id=post_id)
        comments = Comment.objects.all().filter(post=post)
        comments_info = []
        for comment in comments:
            comment_info = {
                "commentId": comment.id,
                "commentContent": comment.content,
                "commentDate": comment.date
            }
            comments_info.append(comment_info)
        return JsonResponse(comments_info, safe=False)


class IMTokenView(APIView):
    @swagger_auto_schema(
        operation_summary='获取用户IMToken',
        response={200: 'OK'}
    )
    def get(self, request):
        user_id = request.session.get('_auth_user_id')
        user = User.objects.get(id=user_id)
        token = user.im_token
        return JsonResponse({"success": True, "token": token})


class AllUnadoptedPetsView(APIView):
    @swagger_auto_schema(
        operation_summary='获取所有未领养宠物',
        response={200: 'OK'}
    )
    def get(self, request):
        adopted_pets = []
        for user in User.objects.all():
            adopted_pets.append(user.pet)
        pets = Pet.objects.all() - adopted_pets
        pets_info = []
        for pet in pets:
            pets_info.append(info.get_pet_info(pet))
        return JsonResponse({"pets_info": pets_info})
