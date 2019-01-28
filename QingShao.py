from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.get('http://192.168.54.212:58088/login/login')
#输入用户名
driver.find_element_by_name('loginname').send_keys('admin')
#输入密码
driver.find_element_by_name('password').send_keys('123456')
#点击登陆
driver.find_element_by_xpath('//*[@id="loginForm"]/a').click()
#最大化窗口
driver.maximize_window()
#点击版本信息
driver.find_element_by_xpath('//*[@id="sub_0"]/li[2]/a').click()
#点击查看按钮
driver.find_element_by_xpath('//*[@id="bslist"]/table/tbody/tr[1]/td[8]/button[2]').click()
sleep(3)
#点击返回按钮
driver.find_element_by_xpath('//*[@id="bscenter"]/div/div[2]/p[1]/button').click()



