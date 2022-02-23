import json 
from datetime             import datetime

from django.http          import JsonResponse
from django.views         import View
from django.db.models     import Q

from users.models         import User 
from .models              import Reservation 
from houses.models        import House
from users.utils          import token_auth

class HouseReservationView(View): 
    @token_auth
    def post(self, request,house_ids):
        try:
           data = json.loads(request.body)
        
           house             = House.objects.get(id=house_ids)
           max_guest         = house.max_guest
           house_id          = data["house_id"] 
           user_id           = data["user_id"] 
           headcount         = data["headcount"] 
            
           check_in  = datetime.strptime(data["check_in"], '%Y-%m-%d')
           check_out = datetime.strptime(data["check_out"], '%Y-%m-%d')
           
           if check_in < datetime.strptime((datetime.now().strftime("%Y-%m-%d")), "%Y-%m-%d"):
                return JsonResponse({"message": "예약을 할 수 없는 날짜입니다"}, status = 403)

           if check_out < check_in:
                return JsonResponse({"message": "체크아웃 날짜를 확인해주세요"}, status = 401) 

           if headcount > max_guest :
               return JsonResponse({"message": "초과된 예약 인원입니다"}, status = 401)   

           if Reservation.objects.filter(Q(user_id=user_id) & Q(check_in__range= [check_in,check_out]) | (Q(user_id=user_id) & Q(check_out__range=[check_in,check_out]))) :
                return JsonResponse({"message":"이미 예약된 날짜입니다"}, status = 403)   

           Reservation(
                user_id   = data["user_id"],
                headcount = data["headcount"],
                check_in  = data["check_in"],
                check_out = data["check_out"],
                house_id  = data["house_id"]
              ).save()

           return JsonResponse({"message":"reservation succeed"}, status = 201)
        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"}, status = 401)        
