from django.urls         import path 
from houses.views        import HouseDetailView 

urlpatterns = [
    path('/<int:house_id>', HouseDetailView.as_view()),
]
