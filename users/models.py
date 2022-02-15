from django.db import models

from core.models import TimeStampModel

class User(TimeStampModel):
    name              = models.CharField(max_length=50)
    email             = models.EmailField(max_length=100, unique=True)
    password          = models.CharField(max_length=200)
    phone_number      = models.CharField(max_length=50)
    profile_image_url = models.CharField(max_length=2000, null=True)
    kakao_id          = models.CharField(max_length=2000, null=True)
    google_id         = models.CharField(max_length=2000, null=True)
    birth_date        = models.DateField()
    
    class Meta:
        db_table = 'users'

class WishList(models.Model):
    user  = models.ForeignKey('User', on_delete=models.CASCADE)
    house = models.ForeignKey('houses.House', on_delete=models.CASCADE)

    class Meta:
        db_table = 'wish_lists'