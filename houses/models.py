from enum import Enum

from django.db import models

class House(models.Model):
    name        = models.CharField(max_length=100)
    description = models.TextField()
    latitude    = models.DecimalField(max_digits=16, decimal_places=14, default=0.0)
    longitude   = models.DecimalField(max_digits=17, decimal_places=14, default=0.0)
    max_guest   = models.IntegerField()
    trap        = models.BooleanField(default=False)
    exit        = models.BooleanField(default=False)
    city        = models.ForeignKey('City', on_delete=models.CASCADE)
    house_type  = models.ForeignKey('HouseType', on_delete=models.CASCADE)
    ghost       = models.ForeignKey('Ghost', on_delete=models.CASCADE, null=True)
    user        = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'houses'

class HouseImage(models.Model):
    image_url = models.CharField(max_length=2000)
    house     = models.ForeignKey('House', on_delete=models.CASCADE)

    class Meta:
        db_table = 'house_images'

class HouseType(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        db_table = 'house_types'

class Ghost(models.Model):
    name  = models.CharField(max_length=30)

    class Meta:
        db_table = 'ghosts'

class Country(models.Model):
    name  = models.CharField(max_length=100)

    class Meta:
        db_table = 'countries'

class City(models.Model):
    name    = models.CharField(max_length=100)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)

    class Meta:
        db_table = 'cities'

class HouseTypeEnum(Enum):
    폐가 = 1
    정신병원 = 2
    교회 = 3
    학교 = 4
    기숙사 = 5 
    공동묘지 = 6
    호텔 = 7
    숲 = 8
    시장 = 9
    폐허 = 10

class GhostEnum(Enum):
    처녀귀신 = 1
    좀비 = 2
    드라큘라 = 3
    유령 = 4
    개발자 = 5
    학생 = 6
    목사 = 7
    연쇄살인마 = 8 
    백작 = 9
    환자 = 10