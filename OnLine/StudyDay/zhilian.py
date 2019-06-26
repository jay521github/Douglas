import requests
from bs4 import BeautifulSoup
import os
if __name__ == '__main__':
    if not os.path.exists('./kongjie'):
        os.mkdir('./kongjie')
    else:
        print('文件夹已存在')

    url='http://www.91kongjie.com/'
    headers = {
        "User-Agent": "Mozilla/5.0(WindowsNT6.3;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/68.0.3440.106Safari/537.36"
    }
    res=requests.get(url=url,headers=headers).text
    soup=BeautifulSoup(res,'lxml')
    page=soup.select('div.bd dt')
    for i in page:
        page_url=i.a.img['src']
        #print(page_url)
        r=requests.get(url=url,headers=headers).content
        ima_namr=page_url.split('/')[-2]+'.jpg'
        path='./kongjie/'+ima_namr

        with open(path,'wb') as fp:
            fp.write(r)
            print(ima_namr,'下载成功')
