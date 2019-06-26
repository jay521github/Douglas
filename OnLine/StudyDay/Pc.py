import requests
from bs4 import BeautifulSoup
if __name__ == '__main__':
    url='http://www.shicimingju.com/book/sanguoyanyi.html'
    headers = {
            "User-Agent": "Mozilla/5.0(WindowsNT6.3;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/68.0.3440.106Safari/537.36"
        }
    res=requests.get(url=url,headers=headers).text
    soup=BeautifulSoup(res,'lxml')
    li=soup.select('.book-mulu>ul>li')
    fp=open('./sanguo.txt','w',encoding='utf-8')
    for i in li:
        page=i.a.string
        page_url='http://www.shicimingju.com'+i.a['href']
        neirong=requests.get(url=page_url,headers=headers).text
        new_soup=BeautifulSoup(neirong,'lxml')
        content=new_soup.find('div',class_='chapter_content')
        conteng_neirong=content.text
        fp.write(page+':'+conteng_neirong+'\n')
        print(page,'爬取成功')


