import requests

try:
    url = "www.cinda.com.cn//bulletin.do?seachtype=list&status=company"
    payload = {'s_dealoffice': '江苏省分公司', 'seachbulltin': 'history'}
    r = requests.post(url, data=payload)
    print(r.text)
except:
    print("Error")

r = requests.post('http://httpbin.org/post', data = {'key':'value'})