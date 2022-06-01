from datetime import timedelta

from django.contrib import auth
from django.db.models import Q
from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.views import APIView

from myapp import image
from myapp.models import *
import myapp.verification as verification
import myapp.openIM as openIM
import myapp.info as info
import logging

from myapp.serializers import UserSerializer, TracePathSerializer

logger = logging.getLogger(__name__)


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


class UserInfo(APIView):
    @swagger_auto_schema(
        operation_summary='获取用户信息',
        response={200: 'OK'}
    )
    def get(self, request):
        user_id = request.session.get('_auth_user_id')
        user = User.objects.get(id=user_id)
        user_info = info.get_user_info(user)
        return JsonResponse(user_info)

    @swagger_auto_schema(
        operation_summary='修改用户信息',
        response={200: 'OK'}
    )
    def post(self, request):
        user_id = request.session.get('_auth_user_id')
        user = User.objects.get(id=user_id)
        user.first_name = request.POST.get("userFirstName")
        user.email = request.POST.get("userEmail")
        user.user_icon_url = request.POST.get("userIconUrl")
        user.user_phone_number = request.POST.get("userPhoneNumber")
        user.save()
        return JsonResponse({"success": True, "message": "用户信息设置成功"})


class LoginView(APIView):
    @swagger_auto_schema(
        operation_summary='用户登录',
        response={200: 'OK'}
    )
    def post(self, request):
        username = request.POST.get("userName")
        password = request.POST.get("userPassword")
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            token = openIM.get_token(user.username)
            return JsonResponse({"success": True, "message": "登录成功", "im_token": token})
        return JsonResponse({"success": False, "message": "用户名或密码错误"})


class RegisterView(APIView):
    @swagger_auto_schema(
        operation_summary='用户注册',
        response={200: 'OK'}
    )
    def post(self, request):
        username = request.POST.get("userName")
        password = request.POST.get("userPassword")
        email = request.POST.get("userEmail")
        if len(User.objects.filter(username=username)) > 0:
            return JsonResponse({"success": False, "message": "用户名已存在"})
        user = User.objects.create_user(username=username, password=password, email=email)
        user.first_name = username
        user.save()
        token = openIM.register(username)
        return JsonResponse({"success": True, "message": "注册成功", "im_token": token})


class LogoutView(APIView):
    @swagger_auto_schema(
        operation_summary='用户注销',
        response={200: 'OK'}
    )
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
        if pet is None:
            return JsonResponse({"success": False, "message": "用户没有宠物"})
        pet_info = info.get_pet_info(pet)
        return JsonResponse({"success": True, "message": "获取宠物信息成功", "pet": pet_info})

    @swagger_auto_schema(
        operation_summary='修改宠物信息,没有则创建',
        response={200: 'OK'}
    )
    def post(self, request):
        user_id = request.session.get('_auth_user_id')
        user = User.objects.get(id=user_id)
        if user.pet is None:
            new_pet = Pet()
            new_pet.save()
            user.pet = new_pet
            user.save()
        pet = user.pet
        pet.pet_name = request.POST.get("petName")
        pet.pet_type = request.POST.get("petType")
        pet.pet_breed = request.POST.get("petBreed")
        pet.pet_gender = request.POST.get("petGender")
        pet.pet_date_of_birth = request.POST.get("petDateOfBirth")
        pet.pet_icon_url = request.POST.get("petIconUrl")
        pet.save()
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
            user.email_valid = True
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
        if not user.email_valid:
            return JsonResponse({"success": False, "message": "用户邮箱未验证"})
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
        posts = Post.objects.all().order_by("-post_date")
        posts_info = []
        for post in posts:
            post_info = info.get_post_info(post)
            posts_info.append(post_info)
        return JsonResponse({"success": True, "message": "获取帖子成功", "posts": posts_info})


class AllCommentsView(APIView):
    @swagger_auto_schema(
        operation_summary='获取所有评论',
        response={200: 'OK'}
    )
    def get(self, request):
        post_id = request.GET.get("postId")
        post = Post.objects.get(post_id=post_id)
        comments = Comment.objects.all().filter(comment_post=post)
        comments_info = []
        for comment in comments:
            comment_info = info.get_comment_info(comment)
            comments_info.append(comment_info)
        return JsonResponse({"success": True, "message": "获取评论成功", "comments": comments_info})


class CommentView(APIView):
    @swagger_auto_schema(
        operation_summary='添加评论',
        response={200: 'OK'}
    )
    def post(self, request):
        user_id = request.session.get('_auth_user_id')
        user = User.objects.get(id=user_id)
        post_id = request.POST.get("postId")
        if post_id is None:
            return JsonResponse({"success": False, "message": "帖子不存在"})
        post = Post.objects.get(post_id=post_id)
        comment = Comment()
        comment.comment_content = request.POST.get("commentContent")
        comment.comment_user = user
        comment.comment_post = post
        comment.comment_date = datetime.now() + timedelta(hours=8)
        comment.save()
        return JsonResponse({"success": True, "message": "评论成功"})


class IMTokenView(APIView):
    @swagger_auto_schema(
        operation_summary='获取用户IMToken',
        response={200: 'OK'}
    )
    def get(self, request):
        user_id = request.session.get('_auth_user_id')
        user = User.objects.get(id=user_id)
        token = openIM.get_token(user.username)
        return JsonResponse({"success": True, "im_token": token})


class AllUnadoptedPetsView(APIView):
    @swagger_auto_schema(
        operation_summary='获取所有未领养宠物',
        response={200: 'OK'}
    )
    def get(self, request):
        adopted_pets = []
        for user in User.objects.all():
            adopted_pets.append(user.pet)
        pets_info = []
        for pet in Pet.objects.all():
            if pet not in adopted_pets:
                pets_info.append(info.get_pet_info(pet))
        return JsonResponse({"success": True, "message": "获取宠物成功", "pets": pets_info})


class PetsView(APIView):
    @swagger_auto_schema(
        operation_summary='获取所有宠物',
        response={200: 'OK'}
    )
    def get(self, request):
        pets_info = []
        for pet in Pet.objects.all():
            pets_info.append(info.get_pet_info(pet))
        return JsonResponse({"success": True, "message": "获取宠物列表成功", "pets": pets_info})


class PostView(APIView):
    @swagger_auto_schema(
        operation_summary='发布帖子',
        response={200: 'OK'}
    )
    def post(self, request):
        user_id = request.session.get('_auth_user_id')
        user = User.objects.get(id=user_id)
        post_title = request.POST.get("postTitle")
        post_content = request.POST.get("postContent")
        img = request.FILES.get("postCover")
        if img is None:
            post_cover = "https://pic.mcatk.com/soto/202205061633426.png"
        else:
            post_cover = image.upload_image(img)
        post = Post(post_user=user, post_title=post_title, post_content=post_content, post_cover=post_cover)
        post.post_date = datetime.now() + timedelta(hours=8)
        post.save()
        return JsonResponse({"success": True, "message": "帖子发布成功"})


class UserPostsView(APIView):
    @swagger_auto_schema(
        operation_summary='获取用户帖子',
        response={200: 'OK'}
    )
    def get(self, request):
        user_id = request.session.get('_auth_user_id')
        user = User.objects.get(id=user_id)
        posts = Post.objects.all().filter(post_user=user).order_by("-post_date")
        posts_info = []
        for post in posts:
            post_info = info.get_post_info(post)
            posts_info.append(post_info)
        return JsonResponse({"success": True, "message": "获取帖子成功", "posts": posts_info})


class UserCommentsView(APIView):
    @swagger_auto_schema(
        operation_summary='获取用户评论',
        response={200: 'OK'}
    )
    def get(self, request):
        user_id = request.session.get('_auth_user_id')
        user = User.objects.get(id=user_id)
        comments = Comment.objects.all().filter(comment_user=user).order_by("-comment_date")
        comments_info = []
        for comment in comments:
            comment_info = info.get_comment_info(comment)
            comments_info.append(comment_info)
        return JsonResponse({"success": True, "message": "获取评论成功", "comments": comments_info})


class UserDeletesPostView(APIView):
    @swagger_auto_schema(
        operation_summary='用户删除帖子',
        responses={200: 'OK'}
    )
    def post(self, request):
        user = User.objects.get(id=request.session.get('_auth_user_id'))
        post_id = request.POST.get("postId")
        post = Post.objects.get(post_id=post_id)
        if post.post_user != user:
            return JsonResponse({"success": False, "message": "无权限删除"})
        post.delete()
        return JsonResponse({"success": True, "message": "删除帖子成功"})


def test(request):
    obj = request.FILES.get("test")
    image.upload_image(obj)
    return JsonResponse({"success": True, "message": "测试成功"})


class ApplicationView(APIView):
    @swagger_auto_schema(
        operation_summary='申请兽医/护工资格认证',
        response={200: 'OK'}
    )
    def post(self, request):
        user_id = request.session.get('_auth_user_id')
        user = User.objects.get(id=user_id)
        application_type = request.POST.get("applicationType")
        img = request.FILES.get("applicationImage")
        application_image = image.upload_image(img)
        application_description = request.POST.get("applicationDescription")
        application = Application(application_user=user, application_type=application_type,
                                  application_image=application_image,
                                  application_description=application_description)
        application.save()
        return JsonResponse({"success": True, "message": "申请成功"})


# admin

class AdminUserView(APIView):
    @swagger_auto_schema(
        operation_summary='通过用户名获取用户信息',
        response={200: 'OK'}
    )
    def get(self, request):
        user_id = request.session.get('_auth_user_id')
        user = User.objects.get(id=user_id)
        if not user.is_staff:
            return JsonResponse({"success": False, "message": "没有权限"})
        username = request.POST.get("username")
        user = User.objects.get(username=username)
        return JsonResponse({"success": True, 'user': info.get_user_info(user)})


class AdminAllUserView(APIView):
    @swagger_auto_schema(
        operation_summary='获取用户全部信息',
        response={200: 'OK'}
    )
    def get(self, request):
        user_id = request.session.get('_auth_user_id')
        user = User.objects.get(id=user_id)
        if not user.is_staff:
            return JsonResponse({"success": False, "message": "没有权限"})
        users = User.objects.all()
        user_list = []
        for user in users:
            user_list.append(info.get_user_info(user))
        return JsonResponse({"success": True, 'users': user_list})


class AdminApplicationListView(APIView):
    @swagger_auto_schema(
        operation_summary='获取申请兽医/护工资格认证列表',
        response={200: 'OK'}
    )
    def get(self, request):
        user_id = request.session.get('_auth_user_id')
        user = User.objects.get(id=user_id)
        if not user.is_staff:
            return JsonResponse({"success": False, "message": "没有权限"})
        applications = Application.objects.all()
        application_list = []
        for application in applications:
            application_list.append(info.get_application_info(application))
        return JsonResponse({"success": True, 'applications': application_list})


class AdminAgreeApplicationView(APIView):
    @swagger_auto_schema(
        operation_summary='通过兽医/护工资格认证申请',
        response={200: 'OK'}
    )
    def post(self, request):
        user_id = request.session.get('_auth_user_id')
        user = User.objects.get(id=user_id)
        if not user.is_staff:
            return JsonResponse({"success": False, "message": "没有权限"})
        application_id = request.POST.get("applicationId")
        application = Application.objects.get(application_id=application_id)
        application_user = application.user
        application_user.user_type = application.application_type
        application_user.save()
        application.delete()
        return JsonResponse({"success": True, "message": "处理成功"})


class AdminRejectApplicationView(APIView):
    @swagger_auto_schema(
        operation_summary='拒绝兽医/护工资格认证申请',
        response={200: 'OK'}
    )
    def post(self, request):
        user_id = request.session.get('_auth_user_id')
        user = User.objects.get(id=user_id)
        if not user.is_staff:
            return JsonResponse({"success": False, "message": "没有权限"})
        application_id = request.POST.get("applicationId")
        application = Application.objects.get(application_id=application_id)
        application.delete()
        return JsonResponse({"success": True, "message": "处理成功"})


class UploadImageView(APIView):
    @swagger_auto_schema(
        operation_summary='上传图片',
        response={200: 'OK'}
    )
    def post(self, request):
        user_id = request.session.get('_auth_user_id')
        user = User.objects.get(id=user_id)
        if not user:
            return JsonResponse({"success": False, "message": "没有权限"})
        img = request.FILES.get("image")
        image_url = image.upload_image(img)
        return JsonResponse({"success": True, "imageUrl": image_url})


class VaccinationView(APIView):
    @swagger_auto_schema(
        operation_summary='兽医添加接种记录',
        response={200: 'OK'}
    )
    def post(self, request):
        user_id = request.session.get('_auth_user_id')
        user = User.objects.get(id=user_id)
        if user.user_type != '兽医':
            return JsonResponse({"success": False, "message": "没有权限"})
        pet_id = request.POST.get("petId")
        pet = Pet.objects.get(pet_id=pet_id)
        pet.pet_vaccination_status = True
        pet.save()
        return JsonResponse({"success": True, "message": "设置成功"})


class TracePathView(APIView):
    @swagger_auto_schema(
        operation_summary='查询追踪记录',
        response={200: 'OK'}
    )
    def get(self, request):
        trace_path_id = request.GET.get("tracePathId")
        trace_path = TracePath.objects.get(trace_path_id=trace_path_id)
        return JsonResponse({"success": True, "tracePath": info.get_trace_path_info(trace_path, complicated=True)})

    @swagger_auto_schema(
        operation_summary='添加追踪记录',
        response={200: 'OK'}
    )
    def post(self, request):
        user_id = request.session.get('_auth_user_id')
        user = User.objects.get(id=user_id)
        trace_path_coordinates = request.POST.get("tracePathCoordinates")
        trace_path_start_time = request.POST.get("tracePathStartTime")
        trace_path_end_time = request.POST.get("tracePathEndTime")
        trace_path_note = request.POST.get("tracePathNote")
        TracePath(trace_path_user=user, trace_path_coordinates=trace_path_coordinates,
                  trace_path_start_time=trace_path_start_time, trace_path_end_time=trace_path_end_time,
                  trace_path_note=trace_path_note).save()
        return JsonResponse({"success": True, "message": "设置成功"})


class TracePathListView(APIView):
    @swagger_auto_schema(
        operation_summary='获取追踪记录列表',
        response={200: 'OK'}
    )
    def get(self, request):
        user_id = request.session.get('_auth_user_id')
        user = User.objects.get(id=user_id)
        trace_paths = TracePath.objects.filter(trace_path_user=user)
        trace_path_list = []
        for trace_path in trace_paths:
            trace_path_list.append(info.get_trace_path_info(trace_path))
        return JsonResponse({"success": True, "tracePaths": trace_path_list})


class ServiceListView(APIView):
    @swagger_auto_schema(
        operation_summary='获取服务列表',
        response={200: 'OK'}
    )
    def get(self, request):
        services = User.objects.filter(Q(user_type='兽医') | Q(user_type='护工'))
        service_list = []
        for service in services:
            service_info = info.get_service_info(service)
            service_info["userScore"] = info.get_service_score(service)
            service_list.append(service_info)
        return JsonResponse({"success": True, "services": service_list})


class ServiceView(APIView):
    @swagger_auto_schema(
        operation_summary='获取服务详情',
        response={200: 'OK'}
    )
    def get(self, request):
        service_id = request.GET.get("userId")
        service = User.objects.get(id=service_id)
        service_info = info.get_service_info(service, complicated=True)
        return JsonResponse({"success": True, "service": service_info})


class ConsultantView(APIView):
    @swagger_auto_schema(
        operation_summary='发起咨询',
        response={200: 'OK'}
    )
    def post(self, request):
        user_id = request.session.get('_auth_user_id')
        user = User.objects.get(id=user_id)
        consultation_title = request.POST.get("consultationTitle")
        consultation_content = request.POST.get("consultationContent")
        consultation_user = request.POST.get("consultationUser")
        img = request.FILES.get("consultationCover")
        if img is None:
            post_cover = "https://pic.mcatk.com/soto/202205061633426.png"
        else:
            post_cover = image.upload_image(img)
        consultation = Consultation(user_1=user, user_2=consultation_user, title=consultation_title,
                                    content=consultation_content, cover=post_cover,
                                    date=datetime.now() + timedelta(hours=8))
        consultation.save()
        return JsonResponse({"success": True, "message": "咨询发起成功"})


class ConsultationReplyView(APIView):
    @swagger_auto_schema(
        operation_summary='回复咨询',
        response={200: 'OK'}
    )
    def post(self, request):
        user_id = request.session.get('_auth_user_id')
        user = User.objects.get(id=user_id)
        consultation_id = request.POST.get("consultationId")
        consultation_reply_content = request.POST.get("consultationReplyContent")
        consultation = Consultation.objects.get(id=consultation_id)
        if consultation is None:
            return JsonResponse({"success": False, "message": "咨询不存在"})
        consultation_reply = ConsultationReply(consultation=consultation, user=user,
                                               content=consultation_reply_content,
                                               date=datetime.now() + timedelta(hours=8))
        consultation_reply.save()
        return JsonResponse({"success": True, "message": "回复成功"})


class UserConsultationsView(APIView):
    @swagger_auto_schema(
        operation_summary='获取用户咨询列表',
        response={200: 'OK'}
    )
    def get(self, request):
        user_id = request.session.get('_auth_user_id')
        user = User.objects.get(id=user_id)
        consultations = Consultation.objects.filter(Q(user_1=user) | Q(user_2=user))
        consultation_list = []
        for consultation in consultations:
            consultation_info = info.get_consultation_info(consultation)
            consultation_list.append(consultation_info)
        return JsonResponse({"success": True, "consultations": consultation_list})


class ConsultationReplyListView(APIView):
    @swagger_auto_schema(
        operation_summary='获取咨询回复列表',
        response={200: 'OK'}
    )
    def get(self, request):
        consultation_id = request.GET.get("consultationId")
        consultation = Consultation.objects.get(id=consultation_id)
        consultation_replies = ConsultationReply.objects.filter(consultation=consultation)
        consultation_reply_list = []
        for consultation_reply in consultation_replies:
            consultation_reply_list.append(info.get_consultation_reply_info(consultation_reply))
        return JsonResponse({"success": True, "consultationReplies": consultation_reply_list})


class RatingView(APIView):
    @swagger_auto_schema(
        operation_summary='评价服务',
        response={200: 'OK'}
    )
    def post(self, request):
        user_id = request.session.get('_auth_user_id')
        rating_by_user = User.objects.get(id=user_id)
        rating_user_id = request.POST.get("ratingUserId")
        rating_user = User.objects.get(id=rating_user_id)
        score = request.POST.get("ratingScore")
        content = request.POST.get("ratingContent")
        if score is None:
            return JsonResponse({"success": False, "message": "评分不能为空"})
        rating = Rating(rating_user=rating_user, rating_by_user=rating_by_user,
                        rating_score=score, rating_content=content,
                        rating_date=datetime.now() + timedelta(hours=8))
        rating.save()
        return JsonResponse({"success": True, "message": "评价成功"})
