import requests
import json
from get_kako_access_token import f_auth_refresh


def send_kakao_message(message):

    tokens = f_auth_refresh()
    url="https://kapi.kakao.com/v2/api/talk/memo/default/send"
    # kapi.kakao.com/v2/api/talk/memo/default/send 

    headers={
        "Authorization" : "Bearer " + tokens
    }

    data={
        "template_object": json.dumps({
            "object_type":"text",
            "text":message,
            "link":{
                "web_url":"www.naver.com"
            }
        })
    }

    response = requests.post(url, headers=headers, data=data)


# send_kakao_message(
#     """ 
#     2022-10-02 : 사이트 P21
#     2022-10-02 : 사이트 P21
#     2022-10-02 : 사이트 P21
#     2022-10-02 : 사이트 P21
#     2022-10-02 : 사이트 P21
#     2022-10-02 : 사이트 P21
#     2022-10-02 : 사이트 P21
#     2022-10-02 : 사이트 P21
#     2022-10-02 : 사이트 P21
#     2022-10-02 : 사이트 P21
#     2022-10-02 : 사이트 P21
#     """
    
# )