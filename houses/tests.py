from enum import Enum

from django.test import Client, TestCase

from houses.models import Country, City, House

class HouseTest(TestCase):
    def setUp(self):
        class HouseTypeEnum(Enum):
            폐가    = 1
            정신병원 = 2
            교회    = 3

        class GhostEnum(Enum):
            처녀귀신 = 1
            좀비    = 2
            드라큘라 = 3

        countries = Country.objects.bulk_create(
            [
                Country(name='대한민국'),
                Country(name='일본')
            ]
        )

        City.objects.bulk_create(
            [
                City(name='서울특별시', country=countries[0]),
                City(name='아이치현', country=countries[1])
            ]
        )

        House.objects.bulk_create(
            [
                House(
                    name='house1',
                    description='This is a house1',
                    latitude=12.1,
                    longitude=12.1,
                    max_guest=3,
                    trap=True,
                    exit=True,
                    city_id=1,
                    house_type_id=HouseTypeEnum.교회.value,
                    ghost_id=GhostEnum.드라큘라.value
                ),
                House(
                    name='house2',
                    description='This is a house2',
                    latitude=34.1,
                    longitude=57.1,
                    max_guest=5,
                    trap=True,
                    exit=False,
                    city_id=2,
                    house_type_id=HouseTypeEnum.정신병원.value,
                    ghost_id=GhostEnum.처녀귀신.value
                )
            ]
        )
    
    def tearDown(self):
        Country.objects.all().delete()
        City.objects.all().delete()
        House.objects.all().delete()

    def test_success_house_view(self):
        client = Client()