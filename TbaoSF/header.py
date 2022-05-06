import requests

f = open('1.txt', 'r')
raw = f.readlines()
length = len(raw)
for i in range(0, length):
    removeEnter = raw[i].split("\n", 1)
    # print(removeEnter[0])
    word = removeEnter[0].split(":", 1)
    # print(word[1])
    newheader = "\"" + word[0] + "\"" + ":" + "\"" + word[1] + "\""
    print(newheader)
url = 'www.baidu.com'
re = requests.post(url, newheader)



