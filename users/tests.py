from django.test import mock, patch

@patch("users.views.requests")
def test_kakao_signin_new_user_success():
    