from django.urls import path

from reservations.views      import HouseReservationView

urlpatterns = [
  path('/<int:house_ids>', HouseReservationView.as_view()),
]
