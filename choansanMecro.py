from email import message
import time
import config
from post_kakao_message import send_kakao_message
from date_funtion import holyday_retrun
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.wait import WebDriverWait
from telegram_send_message import telegram_send_message

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
# options.add_experimental_option("detach", True) # 화면이 꺼지지 않고 유지
# options.add_argument("--headless") # 헤드리스 모드 백그라운드 실행
# options.add_argument("--disable-gpu")
options.add_experimental_option("excludeSwitches", ["enable-logging"]) # 불필요한 메세지 제거
options.add_experimental_option("excludeSwitches", ["enable-automation"]) # 자동화 메세지 제거
service = ChromeService(executable_path="chromedriver.exe")
browser = webdriver.Chrome(service=service, options=options)
browser.get('https://reservation.nowonsc.kr/member/login')
today_day = datetime.now().day

def site_login():
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
    choansan = browser.get('https://reservation.nowonsc.kr/leisure/camping_date?cate1=2')
    time.sleep(3)


def reservation(month):
    ## 예약 가능할 날짜를 반환한다.
    before_month = browser.find_element(By.XPATH,'//*[@id="frm"]/div[1]/div[1]/div[1]/div/div/div[1]')
    display_month = browser.find_element(By.XPATH,'//*[@id="frm"]/div[1]/div[1]/div[1]/div/div/div[2]')
    display_month = display_month.get_attribute('data-nowmonth')
    next_month = browser.find_element(By.XPATH, '//*[@id="frm"]/div[1]/div[1]/div[1]/div/div/div[3]')
    ## 다음달 '>'을 클릭한다. //*[@id="frm"]/div[1]/div[1]/div[1]/div/div/div[3]
    ## 현재표시되고있는 월 //*[@id="frm"]/div[1]/div[1]/div[1]/div/div/div[2]
    ## 이전달 '<'을 클릭한다. //*[@id="frm"]/div[1]/div[1]/div[1]/div/div/div[1]
  
    try:
        if int(display_month) > month:
            before_month.click()
        if int(display_month) < month:
            next_month.click() 
    except:
        pass
                
    time.sleep(1)
    table= browser.find_elements(By.XPATH, '//*[@data-old="0"]')
    message=""
    for i in table:
        data_day=i.get_attribute('data-day')
        if data_day is not None and data_day in holyday_retrun(month):
        # if data_day is not None :
            ## 예약 가능한 날짜를 클릭한다.
            print(data_day)
            # message = message + "%s%s" % (data_day, ": 없음\n")
            i.click()
            time.sleep(1)
            ## 파크캠핑 빌리지 구역 라디오 버튼을 클릭한다.
            park_button=browser.find_element(By.XPATH, '//*[@id="village01"]').click()
            time.sleep(1)
            ## 파크캥핑 빌리지 구역 예약 가능한 지역을 가져온다
            reserve_locate= browser.find_elements(By.XPATH, '//*[@name="village2"]')
            for j in reserve_locate:
                if j.get_attribute('disabled') is None and 'P' in j.get_attribute('data-cseq') and 'm_chk' not in j.get_attribute('id'):
                    print(j.get_attribute('data-cseq'))
                    message = message + data_day + ": " + j.get_attribute('data-cseq') + "\n" 
                    # time.sleep(1)
                    # j.click()
                    # time.sleep(1)
                    # reserve_button = browser.find_element(By.XPATH, '//*[@id="reserved_submit"]').click() 
    if message != "":
        # send_kakao_message(message)
        telegram_send_message(message)

if __name__ == '__main__':
    site_login()
    time.sleep(1)
    
    while True:
       
        reservation(datetime.now().month)
        time.sleep(1)
        reservation(datetime.now().month+1)
        time.sleep(1)
