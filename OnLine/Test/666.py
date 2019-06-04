import requests
from bs4 import BeautifulSoup
import pymysql
class chushihua():
    def __init__(self,keyword,page=1):
        self.keyword=keyword
        self.page=page
    def one(self):
        url='https://piao.qunar.com/ticket/list.htm?keyword=%s&region=&from=mpl_search_suggest&page=%s' % (self.keyword, self.page)
        re=requests.get(url)
        re.encoding='utf-8'
        text=re.text
        bs=BeautifulSoup(text,'html.parser')
        arr=bs.find('div', {'class': 'result_list'}).contents
        for i in arr:
            info=i.attrs
            name = info.get('data-sight-name')
            # 地址
            address = info.get('data-address')
            # 近期售票数
            count = info.get('data-sale-count')
            # 经纬度
            point = info.get('data-point')

            # 起始价格
            price = i.find('span', {'class': 'sight_item_price'})
            price = price.find_all('em')
            price = price[0].text
            db = pymysql.connect(host="172.17.15.63", port=3306, user="root", passwd="bwgj@2018", db="test_sd",charset="utf8")
            cursor = db.cursor()
            sql='INSERT INTO test(name ,address,count ,point,) value ('','','','')'
            cursor.execute(sql)
            db.commit()
            db.rollback()
            db.close()
if __name__ == '__main__':
    citys = ['北京', '上海', '成都', '三亚', '广州', '重庆', '深圳', '西安', '杭州', '厦门', '武汉', '大连', '苏州']
    for i in citys:
        for page in range(1, 5):
            qne = chushihua(i, page=page)
            qne.one()
