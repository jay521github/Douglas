import requests
import os
import re
if __name__ == '__main__':
    if not os.path.exists('./tupian'):
        os.mkdir('./tupian')
    url='https://www.qiushibaike.com/pic/'
    headers = {
        "User-Agent": "Mozilla/5.0(WindowsNT6.3;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/68.0.3440.106Safari/537.36"
    }
    Ima_data=requests.get(url=url,headers=headers).text


    re_data='<div class="thumb">.*?src="(.*?)" alt.*?</div>'
    res=re.findall(re_data,Ima_data,re.S)
    for i in res:
        i='https:'+i
        r=requests.get(url=url,headers=headers).content
        ima_name=i.split('/')[-1]
        imapath='./tupian/'+ima_name
        with open(imapath,'wb') as fp:
            fp.write(r)
            print(ima_name,'下载成功')
