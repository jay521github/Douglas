import requests
from lxml import etree
import os
if __name__ == '__main__':
    abc='index_3.html'
    if not os.path.exists('./4k'):
        os.mkdir('./4k')
    url = 'http://pic.netbian.com/4kmeinv/index_%d.html'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
    }
    for page_nub in range(1,190):
        new_url=format(url%page_nub)
        re=requests.get(url=new_url,headers=headers).text
        tree=etree.HTML(re)
        list=tree.xpath('//div[@class="slist"]//li')
        for li in list:
            img_url = 'http://pic.netbian.com' + li.xpath('./a/img/@src')[0]
            img_name = li.xpath('./a/img/@alt')[0]+'.jpg'
            img_name = img_name.encode('iso-8859-1').decode('gbk')
            img_path='4k/'+img_name
            page_text=requests.get(url=img_url,headers=headers).content
            with open(img_path,'wb') as fp:
                fp.write(page_text)
                print(img_name,'下载成功',len(img_name))

