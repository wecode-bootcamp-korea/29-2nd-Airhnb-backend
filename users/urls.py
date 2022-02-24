from django.urls import path

from users.views import KakaoSignInView

urlpatterns = [
    path('/kakao/signin', KakaoSignInView.as_view()),
    # path('/kakao', KakaoAuthCodeView.as_view())
    ]