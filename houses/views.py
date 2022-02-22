from django.views  import View
from django.http   import JsonResponse

from houses.models import (
                            House,
                            HouseTypeEnum,
                            GhostEnum,
                            Country,
                            City
                            )

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
                            
class OptionView(View):
    def get(self, request):
        results = [
            {
                'house_type': [house_type.name for house_type in HouseTypeEnum]
            },
            {
                'ghost': [ghost.name for ghost in GhostEnum]
            },
            {
                'country': [country.name for country in Country.objects.all()]
            },
            {
                'city': [city.name for city in City.objects.all()]
            }
        ]

        return JsonResponse({'results': results}, status=200)