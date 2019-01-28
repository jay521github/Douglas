import unittest
from time import sleep
from selenium import webdriver
class Web(unittest.TestCase):
    def test(self):
        self.driver=webdriver.Firefox()
        self.driver.get('http://192.168.54.212:58088/login/login')
        self.driver.maximize_window()
        self.driver.find_element_by_xpath("//input[@name='loginname']").send_keys('admin')
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys('123456')
        self.driver.find_element_by_xpath("//a[@class='landbtn']").click()
        sleep(3)
        self.driver.find_element_by_xpath("//a[contains(.,'课程管理')]").click()
        sleep(2)
        self.driver.find_element_by_xpath("//button[contains(.,'上传标准方案')]").click()
        sleep(3)
        self.driver.find_element_by_xpath('html/body/div[4]/div[2]/div/div[2]/form/div[1]/div/div/div[1]/button').click()
        sleep(1)
        self.driver.find_element_by_xpath("html/body/div[4]/div[2]/div/div[2]/form/div[1]/div/div/div[1]/ul/li[1]/div/input").send_keys('180')
        sleep(2)
        self.driver.find_element_by_xpath("html/body/div[4]/div[2]/div/div[2]/form/div[1]/div/div/div[1]/ul/li[34]/a/label/span").click()
        sleep(2)
        updown=self.driver.find_element_by_xpath("//input[@name='file']")
        updown.send_keys('D:\\1.txt')
        print(updown.get_attribute('value'))
        sleep(3)
        self.driver.find_element_by_xpath("//button[contains(.,'确定')]").click()
if __name__ == '__main__':
    unittest.main()
