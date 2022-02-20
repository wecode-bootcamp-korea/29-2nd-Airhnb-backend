import jwt, uuid

from django.views     import View
from django.http      import JsonResponse
from django.conf      import settings

from users.models import User
from users.utils  import KakaoSocial

class KakaoSignIn(View):
    def get(self, request):
        try:
            if request.GET.get('error'):
                return JsonResponse({'message': 'INVALID_CODE'}, status=400)

            auth_code = request.GET.get('code')
            user_data = KakaoSocial(auth_code).get_user_info()

            kakao_id  = user_data['id']
            name      = user_data['kakao_account']['profile']['nickname']
            email     = user_data['kakao_account']['email']

            user, created = User.objects.get_or_create(
                kakao_id = kakao_id,
                defaults = {
                    'name'             : name,
                    'email'            : email,
                    'password'         : uuid.uuid4()
                }
            )

            access_token = jwt.encode(
                {'id': user.id}, settings.SECRET_KEY, settings.ALGORITHM
                )

            status = 201 if created else 200

            return JsonResponse({'access_token': access_token}, status=status)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)