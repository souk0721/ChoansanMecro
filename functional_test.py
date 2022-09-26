from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options)
browser.get('https://reservation.nowonsc.kr/member/login')

assert '노원구' in browser.title

browser.find_element_by_xpath('//*[@id="memberId"]').send_keys('souk0721')
browser.find_element_by_xpath('//*[@id="memberPassword"]').send_keys('shgustjr1!')