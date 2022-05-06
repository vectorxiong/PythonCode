import requests
import json

if __name__ == '__main__':
    # 1. 指定url
    # post请求
    post_url = 'https://fanyi.baidu.com/sug'

    # 2. 进行UA伪装
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'
}
    # 3. post请求参数处理（同get）
    word = input('enter a word:')
    data = {
        'kw':word
    }
    # 4. 请求发送
    respose = requests.post(url=post_url,data=data,headers=headers)

    # 5. 获取响应数据 由浏览器抓包工具可知返回的是json数据
    # 此处若用respose.text  则返回的是字符串
    # print("text",respose.text)
    dic_obj = respose.json()# json()方法返回的是obj(如果确认响应数据是json类型，才可以使用json())
    # print("dic_obj",dic_obj)

    # 6. 持久化存储
    filename = word+'.json'
    fp = open(filename,'w',encoding='utf-8')
    json.dump(dic_obj,fp=fp,ensure_ascii=False) # 拿到的json字符串是不能用ASCII进行编码的

    print('over!!!')
