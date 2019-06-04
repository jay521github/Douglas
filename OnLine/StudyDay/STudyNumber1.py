import unittest
import HTMLTestRunner
from time import *
from selenium import webdriver
class StudyNumber1(unittest.TestCase):
    def setUp(self):
        self.a=webdriver.Firefox()
        self.a.get('https://www.baidu.com/')
        self.a.maximize_window()
    def tearDown(self):
        self.a.quit()
    def test01(self):
        self.a.find_element_by_id('kw').send_keys('soul')
        self.a.find_element_by_id('su').click()
        sleep(3)
        expect=self.a.find_element_by_xpath("//a[contains(.,'Soul 官网')]").text
        practical='Soul 官网'
        self.assertEqual(expect,practical,msg='pass')
    # def suit(self):
    #     suittest=unittest.TestSuite()
    #     suittest.addTest(StudyNumber1('test01'))
    #     return suittest
if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(StudyNumber1("test01"))
    filename = ".\\StudyReport.html"
    fp = open(filename, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="测试报告",description="测试")
    runner.run(suit)
    fp.close()



