"""back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
import myapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', myapp.views.login),
    path('api/register/', myapp.views.register),
    path('api/logout/', myapp.views.logout),
    path('api/setPetInfo/', myapp.views.set_pet_info),
    path('api/getPetInfo/', myapp.views.get_pet_info),
    path('api/getVerificationCode/', myapp.views.get_verification_code),
    path('api/verifyCode/', myapp.views.verify_code),
    path('api/getUserInfo/', myapp.views.get_user_info),
    path('api/setUserInfo/', myapp.views.set_user_info),
    path('api/getAllPost/', myapp.views.get_all_posts),
    path('api/getPostComment/', myapp.views.get_post_comments),
    path('api/getUserIMToken/', myapp.views.get_user_im_token),
    url(r'^', TemplateView.as_view(template_name="index.html")),
]
