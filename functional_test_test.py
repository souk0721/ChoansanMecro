import time
import config
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
service = ChromeService(executable_path="chromedriver.exe")
browser = webdriver.Chrome(service=service, options=options)
browser.get('https://reservation.nowonsc.kr/member/login')
today_day = datetime.now().day


assert '노원구' in browser.title

## ID 위치
id_box = browser.find_element(By.XPATH, '//*[@id="memberId"]').send_keys(config.id)
time.sleep(1)
pw_box = browser.find_element(By.XPATH, '//*[@id="memberPassword"]').send_keys(config.pw)
# WebDriverWait(browser, timeout=10)
time.sleep(1)
## 로그인 클릭
login_click=browser.find_element(By.XPATH, '//*[@id="frm"]/fieldset/div/div[4]/button')
login_click.click()
time.sleep(3)
## 비밀번호 변경 문구
pw_change = browser.find_element(By.XPATH, '//*[@id="frm"]/fieldset/div[2]/div/a')
print(pw_change)
# if pw_change:
#     print('문구발생')
#     pw_change.click()
#     time.sleep(1)



## 초안산 예약 페이지 입장
choansan = browser.get('https://reservation.nowonsc.kr/leisure/camping_date?cate1=2')
time.sleep(3)

## 예약 가능할 날짜를 반환한다.
table= browser.find_elements(By.XPATH, '//*[@data-old="0"]')
for i in table:
    data_day=i.get_attribute('data-day')
    if data_day is not None:
        ## 예약 가능한 날짜를 클릭한다.
        print(data_day)
        i.click()
        time.sleep(1)
        ## 파크캠핑 빌리지 구역 라디오 버튼을 클릭한다.
        park_button=browser.find_element(By.XPATH, '//*[@id="village01"]').click()
        time.sleep(1)
        ## 파크캥핑 빌리지 구역 예약 가능한 지역을 가져온다
        reserve_locate= browser.find_elements(By.XPATH, '//*[@name="village2"]')
        for j in reserve_locate:
            if j.get_attribute('disabled') is None and 'P' in j.get_attribute('data-cseq') and 'm_chk' not in j.get_attribute('id'):
                print(j.get_attribute('id'))
                # time.sleep(1)
                # j.click()
                # time.sleep(1)
                # reserve_button = browser.find_element(By.XPATH, '//*[@id="reserved_submit"]').click()
                
        
                
            
        
            
            
time.sleep(4)
# print(table)

## 39 - 65 
## 파크캠핑 빌리지 구역 방번호 == /html/body/div[3]/div[1]/div[2]/form/div[1]/div[2]/div[2]/div/ul/li[1]/input
## 파크캠핑 빌리지 구역 방번호 == //*[@name="village2"]
## 파크캠핑 빌리지 구역 라디오 버튼 Xpath == //*[@id="village01"]


## 금일을 기준으로 26일 이후에는 다음달을 검색한다.
# if int(today_day)>25:
#     right_click = browser.find_element(By.XPATH,'//*[@id="frm"]/div[1]/div[1]/div[1]/div/div/div[3]')
#     right_click.click()
#     time.sleep(10)
    

    


# browser.find_element(by=By.NAME,value='//*[@id="memberId"]').send_keys('souk0721')
# browser.find_element('//*[@id="memberPassword"]').send_keys('shgustjr1!')