from urllib import response
import jwt, requests

from django.conf import settings
from django.http import JsonResponse

from users.models import User

class KakaoSocial():
    def __init__(self, auth_code):
        self.grant_type   = 'authorization_code'
        self.client_id    = settings.REST_API_KEY
        self.redirect_url = settings.REDIRECT_URI
        self.auth_code    = auth_code
        
    def get_token(self):
        token_url = 'https://kauth.kakao.com/oauth/token?grant_type={0}&client_id={1}&redirect_uri={2}&code={3}'\
                        .format(
                            self.grant_type,
                            self.client_id,
                            self.redirect_url,
                            self.auth_code
                        )
        headers            = {'Content-Type' : 'application/x-www-form-urlencoded'}
        response = requests.post(token_url, headers=headers)

        if response.status_code == 401 :
            return JsonResponse({'message': 'INVALID_CODE'}, status=400)

        kakao_access_token = response.json()['access_token']
        return kakao_access_token

    def get_user_info(self):
        kakao_access_token = self.get_token()
        headers            = {'Authorization': f'Bearer {kakao_access_token}'}

        user_data = requests.post('https://kapi.kakao.com/v2/user/me', headers=headers)

        return user_data.json()

class TokenAuth():
    def token_auth(func):
        def wrapper(self, request, *args, **kwargs):
            try:
                token        = request.headers.get('Authorization', None)
                payload      = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
                request.user = User.objects.get(id=payload['id'])
            except jwt.exceptions.DecodeError:
                return JsonResponse({'message': 'INVALID_TOKEN'}, status=400)
            
            return func(self, request, *args, **kwargs)

        return wrapper