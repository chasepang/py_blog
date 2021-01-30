from django.urls import path
from users.views import RegisterView, ImageCodeView, SmsCodeView, LoginView, LogoutView

urlpatterns = [
    #注册页面路由
    path('register/', RegisterView.as_view(), name='register'),
    #图片验证码路由
    path('imagecode/', ImageCodeView.as_view(), name='imagecode'),
    #短信验证码路由
    path('smscode/', SmsCodeView.as_view(), name='smscode'),
    #登录页面路由
    path('login/', LoginView.as_view(), name='login'),
    #退出登录
    path('logout/', LogoutView.as_view(), name='logout')
]
