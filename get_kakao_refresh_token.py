import requests
import config
import json

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = config.kakaoRestApi
redirect_uri = 'https://example.com/oauth'
authorize_code = config.authorize_code

## 최초 한번만 실행 한다. 실행 후 kakao_code.json 파일에 access_token과 refresh_token을 반환한다.
def f_auth():
    data = {
        'grant_type': 'authorization_code',
        'client_id': rest_api_key,
        'redirect_uri': redirect_uri,
        'code': authorize_code,
        }

    response = requests.post(url, data=data)
    tokens = response.json()
    
    with open("kakao_refresh_code.json", "w") as fp:
        json.dump(tokens, fp)
        # with open("kakao_refresh_code.json", "r") as fp:
        #     ts = json.load(fp)
        #     r_token = ts["refresh_token"]
        #     return r_token

f_auth()
