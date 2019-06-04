import re
import requests
url='http://www.tianqihoubao.com/lishi/nanjing.html'
headers={
"User-Agent":"Mozilla/5.0(WindowsNT6.3;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/68.0.3440.106Safari/537.36"
}
r=requests.get(url,headers).text
result=r'<li><a.*?title="(.*?)</a>'
rr=re.findall(result,r,re.S)
for i in rr:
    print(i)