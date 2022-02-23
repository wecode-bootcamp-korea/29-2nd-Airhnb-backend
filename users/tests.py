from django.test import Client, TestCase
from django.test import mock, patch, MagicMock

from houses.models import User

class HouseTest(TestCase):
    def setUp(self):
        User.objects.create(
            id=1,
            name="test",
            kakao_id="AAAAA"
        )

    @patch("users.urils.requests")
    def test_success_house_view(self, mocked_requests):
        client = Client()

        class MockedResponse:
            def json(self):
                return {
                "id":123456789,
                "kakao_account": { 
                    "profile_needs_agreement": False,
                    "profile": {
                        "nickname": "홍길동",
                        "thumbnail_image_url": "http://yyy.kakao.com/.../img_110x110.jpg",
                        "profile_image_url": "http://yyy.kakao.com/dn/.../img_640x640.jpg",
                        "is_default_image":False
                    },
                    "email_needs_agreement":False, 
                    "is_email_valid": True, 
                    "is_email_verified": True, 
                    "email": "sample@sample.com",
                    "age_range_needs_agreement":False,
                    "age_range":"20~29",
                    "birthday_needs_agreement":False,
                    "birthday":"1130"
                }
            }

        mocked_requests.post = MagicMock(return_value = MockedResponse())

        response = client.get("/users/kakao/signin?code=xxxxxxxxxxxxxxxxxxxxx")

        self.assertEqual(response.json(), "akahskldjfhakjshdfkhkshdfk")
