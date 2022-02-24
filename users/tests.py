from unittest.mock import patch, MagicMock

from django.test import Client, TestCase

from users.models import User

class KakaoSignInTest(TestCase):
    def setUp(self):
        User.objects.create(
            name     = "홍길동",
            kakao_id = 1111
        )

    def tearDown(self):
        User.objects.all().delete()

    @patch("users.utils.requests")
    def test_new_user_signin_success(self, mocked_token_requests, mocked_info_requests):
        client = Client()
        
        class MockedTokenResponse:
            def json(self):
                return {
                    "access_token" : "mocked_access_token"
                }

        class MockedResponse:
            def json(self):
                return {
                        "id":1234,
                        "kakao_account": { 
                            "profile_needs_agreement": False,
                            "profile"                : {
                                "nickname"           : "홍길동",
                                "thumbnail_image_url": "http://yyy.kakao.com/.../img_110x110.jpg",
                                "profile_image_url"  : "http://yyy.kakao.com/dn/.../img_640x640.jpg",
                                "is_default_image"   : False
                            },
                            "email_needs_agreement"    : False,
                            "is_email_valid"           : True,
                            "is_email_verified"        : True,
                            "email"                    : "sample@sample.com",
                            "age_range_needs_agreement": False,
                            "age_range"                : "20~29",
                            "birthday_needs_agreement" : False,
                            "birthday"                 : "1130"
                        }
                    }

        mocked_token_requests.post = MagicMock(return_value = MockedTokenResponse())
        mocked_info_requests.post  = MagicMock(return_value = MockedResponse())

        response = client.get("/users/kakao/signin?code=testcode")
        self.assertEqual(response.status_code, 200)
