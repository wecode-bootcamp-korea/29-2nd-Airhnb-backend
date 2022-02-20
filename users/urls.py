from django.urls import path

from users.views import KakaoSignIn

urlpatterns = [
    path('/kakao/signin', KakaoSignIn.as_view()),
    # path('/kakao', KakaoAuthCodeView.as_view())
    ]