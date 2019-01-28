# #coding=utf-8
#
# from selenium import webdriver
# import time
#
# browser = webdriver.Firefox()
#
# url= 'http://www.baidu.com'
#
# #通过get方法获取当前URL打印
# print("now access %s" %(url))
# browser.get(url)
# time.sleep(2)
# browser.find_element_by_id("kw").send_keys("selenium")
# browser.find_element_by_id("su").click()
# time.sleep(3)
# browser.quit()

#coding=utf-8

from selenium import webdriver
import time

browser = webdriver.Firefox()

#访问百度首页
first_url= 'http://www.baidu.com'
print("now access %s" %(first_url))
browser.get(first_url)
time.sleep(2)

#访问新闻页面
second_url='http://news.baidu.com'
print("now access %s" %(second_url))
browser.get(second_url)
time.sleep(2)

#返回（后退）到百度首页
print("back to  %s "%(first_url))
browser.back()
time.sleep(1)

#前进到新闻页
print("forward to  %s"%(second_url))
browser.forward()
time.sleep(2)

browser.quit()