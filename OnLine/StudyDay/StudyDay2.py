from selenium import webdriver
driver=webdriver.Firefox()
FirstUrl=('http://www.baidu.com')
print('打开第一个 : %s'%(FirstUrl))
driver.get(FirstUrl)
sencondurl=('http://www.taobao.com')
print('第二个网址 ：%s'%(sencondurl))
driver.get(sencondurl)
'''回到百度'''
print('''''')
driver.back()
'''回到淘宝'''
print('''''')
driver.forward()

