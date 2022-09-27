import requests

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = '157ad50a2a9bbb6ce4a74d41881752b8'
redirect_uri = 'https://example.com/oauth'
authorize_code = 'JV1tkvNUrJawAmV2YQpIhGLbyMWZmiKssGijytHTDervVkMvxzCHoEiv76miwpPdi9jRwwo9dVwAAAGDfRW3Fw'

data = {
    'grant_type':'authorization_code',
    'client_id':rest_api_key,
    'redirect_uri':redirect_uri,
    'code': authorize_code,
    }

response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# json 저장
import json
# #1.
# with open(r"C:\Users\user\Desktop\PythonWorkspace\kakao_test\kakao_code.json","w") as fp:
#     json.dump(tokens, fp)

#2.
with open("kakao_code.json","w") as fp:
    json.dump(tokens, fp)


# json 
# import json

# #2.
# with open("kakao_code.json","r") as fp:
#     ts = json.load(fp)
# print(ts)
# print(ts["access_token"])