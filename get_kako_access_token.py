import requests
import config
import json


url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = config.kakaoRestApi
redirect_uri = 'https://example.com/oauth'
authorize_code = config.authorize_code

        
## f_auth()에서 얻은 r_token = refresh_token으로 매번 access_token을 발급받아 활용한다.
def f_auth_refresh():
    with open("kakao_refresh_code.json", "r") as fp:
        ts = json.load(fp)
        data = {
            "grant_type": "refresh_token",
            "client_id": rest_api_key,
            "refresh_token": ts["refresh_token"]
            }
        response = requests.post(url, data=data)
        tokens = response.json()
        with open(r"kakao_access_code.json", "w") as fp:
            json.dump(tokens, fp)
        
        with open("kakao_access_code.json", "r") as fp:
            ts = json.load(fp)
            token = ts["access_token"]
            # print(token)
            return token

f_auth_refresh()