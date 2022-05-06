from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from fake_useragent import UserAgent

driver = webdriver.Firefox()
url = 'https://sf-item.taobao.com/sf_item/627139070419.htm?spm=a213w.7398504.paiList.40.443f3487YumcJr&track_id=cfe0efac-18e7-4b7b-9515-63c60275bed8'

driver.get(url)
wait = WebDriverWait(driver, 4)
Place = driver.find_element_by_xpath('/html/body/div[3]/div[4]/div/div/h1').text
time = driver.find_element_by_xpath('/html/body/div[3]/div[4]/div/div/div[2]/div[1]/ul/li[1]/span[2]').text
Fake_price = driver.find_element_by_xpath('/html/body/div[3]/div[4]/div/div/div[2]/div[5]/table/tbody/tr[1]/td[2]/span[2]/span').text
Real_price = driver.find_element_by_xpath('/html/body/div[3]/div[4]/div/div/div[2]/div[1]/ul/li[2]/div/p[1]/span/em').text
Person_count = driver.find_element_by_xpath('/html/body/div[3]/div[4]/div/div/div[2]/div[4]/span[1]/em').text
count = int(Person_count)
if count > 0:
    print('变卖成功', end=" ")
else:
    print('变卖失败', end=" ")
print('，{}人竞拍'.format(Person_count), end=" ")
print('，'+Place+'，交易时间：'+time+'，评估价格：'+Fake_price+'元'+'，成交价格：'+Real_price+'元，', end=" ")

Fake = Fake_price.replace(',', '')
Real = Real_price.replace(',', '')
R = float(Real)
F = float(Fake)
zhe = round(R/F*10, 2)
print('打折为：', zhe, '折')










