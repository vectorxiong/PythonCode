# coding = utf-8
from selenium import webdriver  # 导入库
browser = webdriver.Firefox()  # 声明浏览器
url = 'http://www.landchina.com/default.aspx?tabid=263'
browser.get(url) # 浏览器预设网址
# time.sleep(3)
browser.delete_all_cookies()
browser.add_cookie({'security_session_high_verify': '231f4b3ac3d86c88bb1deb724274e818', 'security_session_verify': 'a8a79419f5232869c396e6850b34272c'})
print("scuccessOpen")
browser.close()                                   # 关闭浏览器
