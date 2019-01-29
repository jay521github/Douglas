import requests
import re
url=requests.get('http://www.beiwaiqingshao.com/')
a=re.findall('title="(.*?)</a>',url.text)
for b in a:
    print(b)