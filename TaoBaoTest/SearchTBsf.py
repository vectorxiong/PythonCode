from selenium import webdriver
import time
from fake_useragent import UserAgent

driver = webdriver.Firefox()
url = 'https://www.taobao.com/'
#ua = UserAgent()
#headers = {'User-Agent': ua.random}
driver.get(url)
driver.find_element_by_id('q').send_keys('python')
time.sleep(3)
driver.find_element_by_class_name("btn-search").click()
time.sleep(25)

def get_product():
    lis = driver.find_elements_by_xpath('//div[@class="items"]/div[@class="item J_MouserOnverReq  "]')
    for li in lis:
        #info = li.find_element_by_xpath('.//div[@class="row row-2 title"]').text
        price = li.find_element_by_xpath('.//a[@class="J_ClickStat"]').get_attribute('trace-price')+'元'
        #print(info)
        print(price)

get_product()


