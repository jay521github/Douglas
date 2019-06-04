from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
driver=webdriver.Firefox()
driver.get('https://www.baidu.com/')
driver.maximize_window()
First=driver.title
print('这个标题是:%s'%First)
Expect='百度一下，你就知道'
if First==Expect:
    print('正确')
else:
    print('错误')
cook=driver.get_cookies()
print(cook)
driver.quit()