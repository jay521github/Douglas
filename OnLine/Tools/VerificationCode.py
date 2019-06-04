import pytesseract
from selenium import webdriver
from PIL import Image, ImageEnhance
from time import sleep
from OnLine.Tools.singleton import singleton
@singleton
class VerificationCode(object):
    def __init__(self):
        self.driver=webdriver.Chrome()
        loginurl = 'http://tms.beiwaiguoji.com'
        # 截图或验证码图片保存地址
        screenImg = "D:\screenshots\screenImg.png"
        self.driver.get(loginurl)
        #self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.find_element_by_xpath("//input[@name='loginname']").send_keys('admin')
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys('bwgj')
        # 浏览器页面截屏
        self.driver.get_screenshot_as_file(screenImg)
        # 定位验证码位置及大小
        sleep(5)
        location = self.driver.find_element_by_id('validNumberImg').location
        size = self.driver.find_element_by_id('validNumberImg').size
        left = location['x']
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']
        # 从文件读取截图，截取验证码位置再次保存
        img = Image.open(screenImg).crop((left, top, right, bottom))
        img = img.convert('L')  # 转换模式：L | RGB
        img = ImageEnhance.Contrast(img)  # 增强对比度
        img = img.enhance(2.0)  # 增加饱和度
        img.save(screenImg)
        # 再次读取识别验证码
        img = Image.open(screenImg)
        code = pytesseract.image_to_string(img)
        # code= pytesser.image_file_to_string(screenImg)
        self.driver.find_element_by_id("validNumber").send_keys(code.strip())
        print(code.strip())
        try:
            if code==code.strip():
                # 提交登录
                self.driver.find_element_by_xpath("//a[@class='landbtn']").click()
        except:
            print('验证码无法识别')
