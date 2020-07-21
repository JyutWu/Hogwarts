import urllib.request

import requests

reponse=urllib.request.urlopen('http://www.baidu.com')
reponse2=requests.get('http://www.baidu.com')
# print(reponse.status)
# data=reponse.read()
# print(data)
print(reponse2.headers)

