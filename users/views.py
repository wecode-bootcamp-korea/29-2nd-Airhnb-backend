import jwt, uuid

from django.views     import View
from django.http      import JsonResponse
from django.conf      import settings

from users.models import User
from users.utils  import KakaoAPI

class KakaoSignInView(View):
    def get(self, request):
        try:
            if request.GET.get('error'):
                return JsonResponse({'message': 'INVALID_CODE'}, status=400)

            auth_code          = request.GET.get('code')
            kakao              = KakaoAPI(settings.REST_API_KEY)
            kakao_access_token = kakao.get_token(
                auth_code,
                grant_type   = 'authorization_code',
                redirect_uri = settings.REDIRECT_URI
                )
            user_data = kakao.get_user_info(kakao_access_token)
            
            user = User.objects.get_or_create(
                kakao_id = user_data['id'],
                defaults = {
                    'name'             : user_data['kakao_account']['profile']['nickname'],
                    'email'            : user_data['kakao_account']['email'],
                    'password'         : uuid.uuid4()
                }
            )[0]

            access_token = jwt.encode(
                {'id': user.id}, settings.SECRET_KEY, settings.ALGORITHM
                )
            return JsonResponse({'access_token': access_token}, status=200)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=400)