from selenium import webdriver
import unittest
from time import *
from selenium.webdriver.common.action_chains import ActionChains
class OA(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get('http://oa.beiwaiguoji.com/login.jsp')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
    def tearDown(self):
        self.driver.quit()
    def test(self):
        self.driver.find_element_by_xpath("//input[@class='lui_login_input_username']").send_keys('sundong')
        self.driver.find_element_by_xpath("//input[@class='lui_login_input_password']").send_keys('sd19841108')
        self.driver.find_element_by_xpath("//div[@class='lui_login_button_div_c']").click()
        self.driver.find_element_by_xpath("//img[@src='/ui-ext/zidingyi/20301kaoqinxitong.jpg']").click()
        if __name__ == '__main__':
            unittest.main()







