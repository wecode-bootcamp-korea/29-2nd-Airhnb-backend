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
    house = models.ForeignKey('House', on_delete=models.CASCADE, null=True)

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