from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from Test.TesseractPy3 import *
class lgoin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = 'http://192.168.54.212:58088/login/login'  # 要测试的链接
        # self.title = '某管理平台'  # 测试网站的Title
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_lgoin(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.save_screenshot('All.png')  # 截取当前网页，该网页有我们需要的验证码
        imgelement = driver.find_element_by_xpath("//img[@id='validNumberImg']")
        location = imgelement.location  # 获取验证码x,y轴坐标
        size = imgelement.size  # 获取验证码的长宽
        rangle = (int(location['x']), int(location['y']), int(location['x'] + size['width']),
                  int(location['y'] + size['height']))  # 写成我们需要截取的位置坐标
        # im = Image.open("image_path")
        Image.new('RGB', (640, 640))
        i = Image.open("All.png") # 打开截图
        i.convert('RGB')  # this converts png image as jpeg

        result = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
        result.save('result.jpg')
        print('result.jpg')
        text = image_to_string('result.jpg', 'eng').strip()

        # assert self.title in driver.title

        driver.find_element_by_id('loginname').clear()
        driver.find_element_by_id('loginname').send_keys('admin')  # 用户名
        driver.find_element_by_id("Password").clear()
        driver.find_element_by_id("Password").send_keys('123456')  # 密码
        # driver.find_element_by_name('verifyCode').clear()
        driver.find_element_by_name('validNumber').send_keys(text)
        driver.find_element_by_xpath("//a[@class='landbtn']").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        # self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
