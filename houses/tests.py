from django.test    import TestCase, Client

from users.models  import User
from houses.models import City, Country, Ghost, House, HouseType

class HostTest(TestCase):
    def setUp(self):
        test_user = User.objects.create(
                id                  = 1,
                name                = "test",
                email               = "test@kakao.com",
                password            = "123456789",
                phone_number        = "010-0000-0000",
                profile_image_url   = "test_url",
                kakao_id            = "test_kakao_id",
                google_id           = "test_google_id",
                birth_date          = "1999-01-01"
            )

        test_country    = Country.objects.create(name="test_country")
        test_city       = City.objects.create(name="test_city", country_id=test_country.id)
        test_house_type = HouseType.objects.create(name="test_house_type")
        test_ghost      = Ghost.objects.create(name="test_ghost")

        House.objects.create(
            id          = 1,
            name        = "test",
            description = "test_text",
            latitude    = 12.3456,
            logitude    = 98.7654,
            max_guest   = "5",
            trap        = True,
            exit        = False,
            city        = test_city,
            house_type  = test_house_type,
            ghost       = test_ghost,
            user        = test_user,
        )

    def tearDown(self):
        User.objects.all().delete()
        Country.objects.all().delete()
        City.objects.all().delete()
        HouseType.objects.all().delete()
        Ghost.objects.all().delete()
        House.objects.all().delete()


    
