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
# if pw_change:
#     print('문구발생')
#     pw_change.click()
#     time.sleep(1)
## 초안산 예약 페이지 입장
choansan = browser.get('https://reservation.nowonsc.kr/leisure/camping_date?cate1=2')
time.sleep(3)

## 금일을 기준으로 26일 이후에는 다음달을 검색한다.
if int(today_day)>25:
    right_click = browser.find_element(By.XPATH,'//*[@id="frm"]/div[1]/div[1]/div[1]/div/div/div[3]')
    right_click.click()
    time.sleep(10)
    

    


# browser.find_element(by=By.NAME,value='//*[@id="memberId"]').send_keys('souk0721')
# browser.find_element('//*[@id="memberPassword"]').send_keys('shgustjr1!')