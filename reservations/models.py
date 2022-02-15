from django.db import models

from core.models import TimeStampModel

class Reservation(TimeStampModel):
    check_in  = models.DateField()
    check_out = models.DateField()
    headcount = models.IntegerField()
    user      = models.ForeignKey('users.User', on_delete=models.CASCADE)
    house     = models.ForeignKey('houses.House', on_delete=models.CASCADE)

    class Meta:
        db_table = 'reservations'