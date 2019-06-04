from selenium import webdriver
from PIL import Image
import pytesseract
import os,time
driver=webdriver.Firefox()
driver.get('http://dev.beiwaiguoji.com')
driver.maximize_window()
driver.refresh()
driver.save_screenshot('a.png')
location = driver.find_element_by_id('validNumberImg').location
size = driver.find_element_by_id('validNumberImg').size
left = location['x']
top = location['y']
right = location['x'] + size['width']
bottom = location['y'] + size['height']
a = Image.open("a.png")
im = a.crop((left,top,right,bottom))
im.save('a.png')
time.sleep(1)
#打开保存的验证码图片
image = Image.open("a.png")
#图片转换成字符
vcode = pytesseract.image_to_string(image)
print(vcode)
#填充用户名 密码 验证码
driver.find_element_by_xpath("//input[@name='loginname']").send_keys('shenfenghua')
driver.find_element_by_xpath("//input[@name='password']").send_keys('123456')
driver.find_element_by_id("validNumber").send_keys(vcode)
#点击登录
time.sleep(2)
driver.find_element_by_xpath("//a[@class='landbtn']").click()