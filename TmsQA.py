import unittest
from time import *
from OnLine.Tools.VerificationCode import VerificationCode
class Tms(unittest.TestCase):
    def setUp(self):
        self.driver=VerificationCode().driver
    def tearDown(self):
        self.driver.quit()
    def test01(self):
        self.driver.implicitly_wait(10)
        js = "window.scrollTo(0,document.body.scrollHeight)"  # 滚动到底部
        self.driver.execute_script(js)
        self.driver.find_element_by_xpath("//a[contains(.,'TMS问题管理')]").click()
        js = "window.scrollTo(0,document.body.scrollTop=0)"
        self.driver.execute_script(js)
        sleep(2)
        self.driver.find_element_by_xpath('html/body/div[2]/div[2]/div/div[2]/div[1]/form/div[2]/div/div[2]/button').click()
        sleep(1)
        self.driver.find_element_by_xpath('html/body/div[2]/div[2]/div/div[2]/div[1]/form/div[2]/div/div[2]/ul/li[3]/a/label/span').click()
        sleep(1)
        self.driver.find_element_by_xpath("//button[contains(.,'查询')]").click()
        #a=self.driver.find_element_by_xpath("//li[contains(.,'没有数据！')]").text
if __name__ == '__main__':
    unittest.main()
