import json, boto3

from django.http      import JsonResponse
from django.views     import View
from django.db        import transaction
from django.conf      import settings

from houses.models    import Country, House, HouseImage, City, HouseTypeEnum, GhostEnum
from core.storages    import ImageUploader, ImageHandler
from users.utils      import token_auth

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

boto3_client = boto3.client(
    's3',
    aws_access_key_id     = settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key = settings.AWS_SECRET_ACCESS_KEY
)

image_uploader = ImageUploader(boto3_client, settings.AWS_STORAGE_BUCKET_NAME)

class HouseTypeView(View):
    def get(self, request):
        data = [{
            "house_type_id"   : house_type.value,
            "house_type_name" : house_type.name
        } for house_type in HouseTypeEnum]
        return JsonResponse({"message" : data}, status=200)

class GhostView(View):
    def get(self, request):
        data = [{
            "ghost_id"   : ghost.value,
            "ghost_name" : ghost.name
        } for ghost in GhostEnum]
        return JsonResponse({"message" : data}, status=200)

class HostView(View):
    @token_auth
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        try:
            house_images = request.FILES.getlist("house_images")

            if len(house_images) < 2:
                return JsonResponse({"message" : "At least two house_images are required"}, status=400)

            user    = request.user
            country = request.POST["country"]
            city    = request.POST["city"]

            country, is_country_created = Country.objects.get_or_create(name=country)
            city, is_city_created       = City.objects.get_or_create(
                    name          = city, 
                    country__name = country.name,
                    country_id    = country.id
                )

            house = House.objects.create(
                name          = request.POST["name"],
                description   = request.POST["description"],
                latitude      = request.POST["latitude"],
                longitude     = request.POST["longitude"],
                max_guest     = request.POST["max_guest"],
                trap          = request.POST["trap"],
                exit          = request.POST["exit"],
                city          = city,
                house_type_id = request.POST["house_type_id"],
                ghost_id      = request.POST["ghost_id"],
                user          = user
            )

            for image in house_images:
                folder_name   = 'house'
                image_handler = ImageHandler(image, folder_name, image_uploader)
                image_url     = image_handler.save()
                HouseImage(
                    image_url = image_url,
                    house     = house
                ).save()
            return JsonResponse({"message" : "SUCCESS"}, status=201)
        except KeyError:
            return JsonResponse({"message" : "KEY ERROR"}, status=400)
        except Exception as e:
            return JsonResponse({"message" : getattr(e,"message",str(e))}, status=400)