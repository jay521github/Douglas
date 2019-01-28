import unittest
import pytesseract
from selenium import webdriver
from PIL import Image, ImageEnhance
from time import sleep
from HTMLTestRunner import HTMLTestRunner
class VerificationCode(unittest.TestCase):
    def test(self):
        self.driver=webdriver.Chrome()
        loginurl = 'http://dev.beiwaiguoji.com'
        # 截图或验证码图片保存地址
        screenImg = "D:\screenshots\screenImg.png"
        self.driver.get(loginurl)
        #self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.find_element_by_xpath("//input[@name='loginname']").send_keys('admin')
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys('123456')
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
            self.driver.find_element_by_xpath("//input[@name='loginname']").send_keys('admin')
            self.driver.find_element_by_xpath("//input[@name='password']").send_keys('123456')
            self.driver.find_element_by_xpath("//a[@class='landbtn']").click()
        # sleep(3)
        # '''游戏更新'''
        # self.driver.find_element_by_xpath("//a[contains(.,'游戏更新')]").click()#点击游戏更新
        # sleep(2)
        # self.driver.find_element_by_xpath("//button[contains(.,'添加')]").click()#点击添加
        # sleep(2)
        # self.driver.find_element_by_xpath("//input[@name='title']").send_keys('自动化游戏包添加测试')
        # self.driver.find_element_by_xpath("//textarea[@check-type='required']").send_keys('Test')
        # sleep(3)
        # self.driver.find_element_by_xpath("//input[@name='file']").send_keys('D:\\games.zip')
        # sleep(5)
        # self.driver.find_element_by_xpath("//button[contains(.,'确定')]").click()
        # sleep(5)
        # updata=self.driver.find_element_by_xpath('html/body/div[2]/div[2]/div/div[2]/div/table/tbody/tr[1]/td[4]').text
        # result='Test'
        # try:
        #     if updata==result:
        #         print('UpData is ok')
        # except:
        #     print('UpData is Error')

if __name__ == '__main__':
    Suite=unittest.TestSuite()
    Suite.addTest(VerificationCode('test'))
    failepath='D:\Html\\GameTest.html'
    fp=open(failepath,'wd')
    runner=HTMLTestRunner(stream=fp,verbosity=3,title='自动化测试用例',description='测试用例')
    runner.run(Suite)
    fp.close()
