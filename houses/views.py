import json

from django.views            import View
from django.http             import JsonResponse

from .models                 import House, HouseImage, HouseType, Ghost ,Country,City
from reservations.models     import Reservation



class HouseDetailView(View):
    def get(self, request, house_id):
    
        house = House.objects.get(id=house_id)
        
        
        result = {
                'house_id': house.id,
                'name' : house.name,
                'description' : house.description,
                'latitude' : house.latitude,
                'longitude': house.longitude,
                'house_type': house.house_type.name,
                'max_guest' : house.max_guest,
                'country': house.city.country.name,
                'city' : house.city.name,
                'reservation': list(house.reservation_set.all().values()),
                'trap' : house.trap,
                'exit' : house.exit,
                'houseimage' : [
                    houseimage.image_url
                        for houseimage in house.houseimage_set.all()],
        } 

        return JsonResponse({'result' : result}, status = 200)