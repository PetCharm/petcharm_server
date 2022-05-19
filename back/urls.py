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
from rest_framework import permissions, routers

import myapp.views

schema_view = get_schema_view(
    openapi.Info(
        title="PetCharm API",
        default_version='0.1',
        description="欢迎来到PetCharm接口文档",
        terms_of_service="http://43.138.31.99/doc/",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
# router.register(r'users', myapp.views.UserViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^doc(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api/login/', myapp.views.LoginView.as_view()),
    path('api/register/', myapp.views.RegisterView.as_view()),
    path('api/logout/', myapp.views.LogoutView.as_view()),
    path('api/verificationCode/', myapp.views.VerificationCodeView.as_view()),
    path('api/user/', myapp.views.UserInfo.as_view()),
    path('api/comment/list/', myapp.views.AllCommentsView.as_view()),
    path('api/comment/', myapp.views.CommentView.as_view()),
    path('api/IMToken/', myapp.views.IMTokenView.as_view()),
    path('api/retrievePassword/', myapp.views.RetrievePasswordView.as_view()),
    path('api/retrievePasswordVerificationCode/', myapp.views.RetrievePasswordVerificationCodeView.as_view()),
    path('api/pet/', myapp.views.PetView.as_view()),
    path('api/pet/unadopted/', myapp.views.AllUnadoptedPetsView.as_view()),
    path('api/pet/list/', myapp.views.PetsView.as_view()),
    path('api/pet/vaccinate/', myapp.views.VaccinationView.as_view()),
    path('api/post/', myapp.views.PostView.as_view()),
    path('api/post/list/', myapp.views.AllPostsView.as_view()),
    path('api/post/user/', myapp.views.UserPostsView.as_view()),
    path('api/post/delete/', myapp.views.UserDeletesPostView.as_view()),
    path('api/test/', myapp.views.test),
    path('api/user/apply/', myapp.views.ApplicationView.as_view()),
    path('api/admin/userInfo/', myapp.views.AdminUserView.as_view()),
    path('api/admin/allUsers/', myapp.views.AdminAllUserView.as_view()),
    path('api/admin/allApplications/', myapp.views.AdminApplicationListView.as_view()),
    path('api/admin/application/agree/', myapp.views.AdminAgreeApplicationView.as_view()),
    path('api/admin/application/reject/', myapp.views.AdminRejectApplicationView.as_view()),
    path('api/uploadImage/', myapp.views.UploadImageView.as_view()),
    url(r'^', TemplateView.as_view(template_name="index.html")),
]

