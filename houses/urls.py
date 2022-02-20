from django.urls import path

from houses.views import HouseView, OptionView

urlpatterns = [
    path('', HouseView.as_view()),
    path('/options', OptionView.as_view()),
    ]