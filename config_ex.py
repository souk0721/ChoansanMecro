
## 초안산 사이트
id = 'id'
pw = 'pw'

## kakao
kakaoRestApi = 'rest_api_key'
kakaoAPIURL = 'https://kauth.kakao.com/oauth/authorize?client_id="rest_api_key"&redirect_uri=https://example.com/oauth&response_type=code'
authorize_code = 'authorize_code'

## 텔레그램
telegram_bot_id = "telegram_bot_id"
telegram_user = "telegram_user"
telegram_channel = "telegram_channel" 
telegram_token = 'telegram_token'

###
# 1. kakaoAPIURL로 접속하면 'code=' 다음부터 authorize_code가 발행됨
# 2. authorize_code는 한달동안 유효하다. config.py authorize_code = 에 발급받은 코드를 삽입
# 3. get_kakao_refresh_token.py를 한번만 실행해준다. 한번이상실행하면 1번부터 다시해야한다.(한달에1번) 
#  ** 주의사항 authorize_code를 가지고 post로 중복으로 보내면 에러가 발생한다. 다시 1번으로 돌아가서
#  ** 새로운 authorization_code를 재발급 받아서 사용한다.



