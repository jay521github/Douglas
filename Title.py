from selenium import webdriver
driver=webdriver.Firefox()
driver.get('http://192.168.54.212:58088/login/login')
a=driver.title
print('这个标题是小付%s'%a)