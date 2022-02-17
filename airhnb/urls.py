from django.urls import path, include

urlpatterns = [
    path('houses', include('houses.urls')),
    path('users', include('users.urls'))
]