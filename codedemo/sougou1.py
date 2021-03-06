import  requests

if __name__ == "__main__":
    # 1. 指定url
    url = "https://www.sogo.com/"
    # 2. 发起请求
    response = requests.get(url=url)
    # get方法灰返回一个响应对象
    # 3. 获取相应数据 .text返回的是字符串形式的响应数据
    page_text = response.text
    print(page_text)
    # 4. 持久化存储 --page_text
    with open('./sogo.html', 'w',encoding='utf-8') as fp:
        fp.write(page_text)
    print('爬取数据结束')
