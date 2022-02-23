from urllib import response
import jwt, requests

from django.conf import settings
from django.http import JsonResponse

from users.models import User

class KakaoAPI:
    def __init__(self, client_id):
        self.client_id = client_id
        
    def get_token(self, auth_code, **kwargs):
        grant_type   = kwargs['grant_type']
        redirect_uri = kwargs['redirect_uri']
        outh_url     = f'https://kauth.kakao.com/oauth/token?grant_type={grant_type}&client_id={self.client_id}&redirect_uri={redirect_uri}&code={auth_code}'
        headers      = {'Content-Type' : 'application/x-www-form-urlencoded'}
        response     = requests.post(outh_url, headers=headers)

        if response.status_code == 401 :
            raise Exception('INVALID_AUTH_CODE')

        return response.json()['access_token']

    def get_user_info(self, kakao_access_token):
        headers  = {'Authorization': f'Bearer {kakao_access_token}'}
        outh_url = 'https://kapi.kakao.com/v2/user/me'
        response = requests.post(outh_url, headers=headers)

        if response.status_code != 200:
            raise Exception('INVALID_TOKEN')

        return response.json()

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