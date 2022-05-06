from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
import os

driver = webdriver.Chrome()
url = 'https://www.landchina.com/default.aspx?tabid=263'
driver.maximize_window()
wait = WebDriverWait(driver, 10)
driver.get(url)
time.sleep(15)
js = 'document.getElementById("TAB_queryTblEnumItem_212_v").setAttribute("value","07")'
driver.execute_script(js)
driver.find_element_by_id("TAB_QueryConditionItem212").click()
driver.find_element_by_id('TAB_queryTextItem_269').send_keys('萧县')
time.sleep(3)
driver.find_element_by_class_name("HeadToolButton").click()
'''
step1 定位到整个表格
step2 获取一共有多少行
step3 根据有多少行来判断需要点击多少次超链接
step4 点击进去第一行超链接，进行数据提取
step5 关闭当前页面
step6 又定位到第一个页面再点击第二个链接提取数据，直到最后一个
'''
#定位到表格，并打印表格内容
tb = driver.find_element_by_name("contentTable")
rows = tb.find_elements_by_tag_name("tr")
length = len(rows)
print(length)
#找到所有的表格中的a标签
hrfss = driver.find_elements_by_xpath("/html/body/form/font/table/tbody/tr[4]/td/table/tbody/tr/td/table[2]/tbody/tr[1]/td/table[2]/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td[3]/table[2]/tbody/tr[1]/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/table/tbody//a")
# for i in range(1, length):
#     # hf.click()
#     # time.sleep(3)
#     # 获取所有的窗口
#     # res = hf.get_attribute("href")
#     # print(res)
#     driver.find_element_by_partial_link_text('萧县').click()
#     all_h = driver.window_handles
#     # 根据列表下标锁定
#     driver.switch_to.window(all_h[1])
for hrf in hrfss:
    hrf.click()

# hrfs = driver.find_elements_by_tag_name("a")
# for hrf in hrfs:
#     print(hrf.get_attribute("href"))
# tr_content = tb.find_elements_by_tag_name("tr")
# for tr in tr_content:
#     print(tr.text)
# tb = driver.find_elements_by_id("//table[@id='TAB_contentTable']")
# print(tb)
# def get_info():
#     lis = driver.find_elements_by_xpath('//tr[@onmouseout="this.className=rowClass"]')
#     for li in lis:
#         hrf = li.find_element_by_xpath('.//td[@class="queryCellBordy"]//a').get_attribute('href')
#
#
# get_info()
# list_a = driver.find_elements_by_tag_name("a")
# print(list_a)
# for i in range(0, 3):
#     lings = driver.find_elements_by_tag_name("a")
#     lin = lings[i]
#     lin.click()
    # time.sleep(4)
    # windows = driver.window_handles
    # driver.switch_to.window(windows([i+1]))
    # driver.close()
    # windows = driver.window_handles
    # driver.switch_to.window(windows([i]))





