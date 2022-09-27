# import requests

# url = 'https://kauth.kakao.com/oauth/token'
# rest_api_key = 'e30070d81a8fb48b14c1a81a9ca81007'
# redirect_uri = 'https://example.com/oauth'
# authorize_code = '0YG48JUT-3346ackOP6fbxKRrrqAZT99S7TVJaQZyCPbobO3EZacYvN6yM54Dmy9byvqtQopcBQAAAGDfMctGg'

# data = {
#     'grant_type':'authorization_code',
#     'client_id':rest_api_key,
#     'redirect_uri':redirect_uri,
#     'code': authorize_code,
#     }

# response = requests.post(url, data=data)
# tokens = response.json()
# print(tokens)

# # json 저장
# import json
# # #1.
# # with open(r"C:\Users\user\Desktop\PythonWorkspace\kakao_test\kakao_code.json","w") as fp:
# #     json.dump(tokens, fp)

# #2.
# with open("kakao_code.json","w") as fp:
#     json.dump(tokens, fp)


# json 읽어오기
# import json

# #2.
# with open("kakao_code.json","r") as fp:
#     ts = json.load(fp)
# print(ts)
# print(ts["access_token"])
import requests
import json

#2.
with open("kakao_code.json","r") as fp:
    tokens = json.load(fp)

url="https://kapi.kakao.com/v2/api/talk/memo/default/send"

# kapi.kakao.com/v2/api/talk/memo/default/send 

headers={
    "Authorization" : "Bearer " + tokens["access_token"]
}

data={
    "template_object": json.dumps({
        "object_type":"text",
        "text":"Hello, world!",
        "link":{
            "web_url":"www.naver.com"
        }
    })
}

response = requests.post(url, headers=headers, data=data)

print(str(response.json()))
