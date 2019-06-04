import requests
import re

url='http://maoyan.com/board/4?offset'
headers={
"User-Agent":"Mozilla/5.0(WindowsNT6.3;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/68.0.3440.106Safari/537.36"
}
r=requests.get(url,headers=headers)
s=r.text
result='<a.*?title="(.*?)" class=.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
pattern=re.findall(result,s,re.S)
for i in pattern:
    print(i)

