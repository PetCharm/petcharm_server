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
from django.db import router
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from drf_yasg import openapi
from drf_yasg.renderers import OpenAPIRenderer, SwaggerUIRenderer
from drf_yasg.views import get_schema_view
from rest_framework import permissions

import myapp.views

schema_view = get_schema_view(
    openapi.Info(
        title="PetCharm API",
        default_version='0.1',
        description="欢迎来到PetCharm接口文档",
        terms_of_service="http://43.138.31.99/doc/",
        contact=openapi.Contact(email="z@mcac.cc"),
        license=openapi.License(name="43.138.31.99"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r'^doc(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
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
    path('api/getVerificationCodeWithUsername/', myapp.views.get_verification_code_with_username),
    path('api/verifyCodeAndChangePassword/', myapp.views.verify_code_and_change_password),
    path('api/getAllUnadoptedPets/', myapp.views.get_all_unadopted_pets),
    url(r'^', TemplateView.as_view(template_name="index.html")),
]
