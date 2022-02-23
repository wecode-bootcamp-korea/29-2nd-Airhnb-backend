from datetime import datetime, timedelta

from django.http      import JsonResponse
from django.views     import View
from django.db.models import Q, Count, Avg

from houses.models import (
                            Country,
                            House,
                            City,
                            HouseTypeEnum,
                            GhostEnum
                            )

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

class HouseView(View):
    def get(self, request):
        # house_type  = request.GET.getlist('house_type',None)
        # ghost       = request.GET.getlist('ghost',None)
        # country     = request.GET.getlist('country',None)
        # city        = request.GET.getlist('city', None)
        # trap        = request.GET.get('trap', None)
        # exit        = request.GET.get('exit', None)
        check_in    = request.GET.get('check_in', None)
        check_out   = request.GET.get('check_out', None)
        headcount   = request.GET.get('headcount', None)
        limit       = int(request.GET.get('limit', '10'))
        offset      = int(request.GET.get('offset', '0'))

        filter_options = {
            'house_type': 'house_type__name__in',
            'ghost'     : 'ghost__name__in',
            'country'   : 'city__country__name__in',
            'city'      : 'city__name__in',
            'trap'      : 'trap__in',
            'exit'      : 'exit__in'
        }

        filter_set = {
            filter_options.get(key): value for (key, value) in dict(request.GET).items() if filter_options.get(key)
        }

        reservation = Q()

        # if house_type:
        #     options &= Q(house_type__name__in=house_type)
        # if ghost:
        #     options &= Q(ghost__name__in=ghost)
        # if country:
        #     options &= Q(city__country__name__in=country)
        # if city:
        #     options &= Q(city__name__in=city)
        # if trap:
        #     options &= Q(trap=trap)
        # if exit:
        #     options &= Q(exit=exit)
        if check_in and check_out:
            check_in  = datetime.strptime(check_in, '%Y-%m-%d')
            check_out = datetime.strptime(check_out, '%Y-%m-%d')
            
            reservation &= Q(reservation__check_in__range=(check_in, check_out-timedelta(days=1)))
            reservation &= Q(reservation__check_out__range=(check_in, check_out-timedelta(days=1)))
        if headcount:
            reservation &= Q(max_guest__lt=headcount)

        houses = House.objects.filter(**filter_set)\
                        .exclude(reservation)\
                        .select_related('user')\
                        .select_related('ghost')\
                        .prefetch_related('houseimage_set')\
                        .prefetch_related('review_set')

        results = [
            {
                'house_id'        : house.id,
                'name'            : house.name,
                'house_image'     : [image.image_url for image in house.houseimage_set.all()],
                'lat'             : house.latitude,
                'lng'             : house.longitude,
                'user_name'       : house.user.name if house.user else None,
                'review_average'  : house.review_set.aggregate(total=Avg('fear_rating')),
                'review_count'    : house.review_set.aggregate(total=Count('fear_rating')),
                'trap'            : house.trap,
                'exit'            : house.exit,
                'ghost'           : house.ghost.name if house.ghost else None,
                'city'            : house.city.name,
                'country'         : house.city.country.name,
                'house_type'      : house.house_type.name
            } for house in houses[offset:offset+limit]
        ]

        total_pages = houses.aggregate(total=Count('name'))['total']

        return JsonResponse({
            'results'    : results,
            'total_pages': total_pages
            },
            status=200)