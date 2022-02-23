from django.urls         import path 
from houses.views        import (
                                HouseDetailView,
                                OptionView,
                                GhostView,
                                HostView,
                                HouseTypeView,
                                HouseListView
                                )

urlpatterns = [
    path('/<int:house_id>', HouseDetailView.as_view()),
    path('/options', OptionView.as_view()),
    path('/host', HostView.as_view()),
    path('/housetype', HouseTypeView.as_view()),
    path('/ghost', GhostView.as_view()),
    path('', HouseListView.as_view()),
]