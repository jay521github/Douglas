import os,requests
from lxml import etree
if __name__ == '__main__':
    url='https://sou.zhaopin.com/?jl=530&kw=java&kt=3&sf=0&st=0'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
    }
    re=requests.get(url=url,headers=headers).text
    tree=etree.HTML(re)
    list=tree.xpath('')