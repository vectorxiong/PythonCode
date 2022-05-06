import requests

if __name__ == '__main__':
    # UA伪装：将对应的User-Agent封装到一个字典中
    # 伪装成Google浏览器
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'
    }

    # 1. 指定url
    url = 'https://www.sogou.com/sogou?'
    # 'https://www.sogou.com/sogou?query=波晓张'这样也可以的
    # 处理url携带的参数  通常情况url不可能只携带一组参数
    # 处理：封装到字典中
    key = input('enter a word:')
    param = {
        'query': key
    }

    # 2. 对指定的url发起请求 对应的url是携带参数的，并且请求过程中处理了参数
    response = requests.get(url, params=param, headers=headers)

    # 3. 获取响应数据
    page_txt = response.text

    filename = key + '.html'
    with open(filename, 'w', encoding='utf-8') as fp:
        fp.write(page_txt)
    print(filename, '保存成功！！！')
