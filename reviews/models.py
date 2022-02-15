from django.db import models

from core.models import TimeStampModel

class Review(TimeStampModel):
    content     = models.TextField()
    fear_rating = models.DecimalField(max_digits=2, decimal_places=1)
    user        = models.ForeignKey('users.User', on_delete=models.CASCADE)
    house       = models.ForeignKey('houses.House', on_delete=models.CASCADE)

    class Meta:
        db_table = 'reviews'