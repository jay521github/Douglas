import requests
import re
html=requests.get('https://tieba.baidu.com/index.html')
a=re.findall('"img_title">(.*?)</p>',html.text)
for b in a:
    print(b)