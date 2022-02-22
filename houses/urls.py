from django.urls         import path 
from houses.views        import HouseDetailView, OptionView

urlpatterns = [
    path('/<int:house_id>', HouseDetailView.as_view()),
    path('/options', OptionView.as_view()),
]