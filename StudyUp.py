import unittest
from selenium import webdriver
import time
from HTMLTestRunner import HTMLTestRunner
class WebTest(unittest.TestCase):
    def setUp(self):
        self.a=webdriver.Firefox()
        self.a.get('http://www.baidu.com')
        self.a.maximize_window()
    def tearDown(self):
        self.a.quit()
    def test(self):
        self.a.find_element_by_xpath("//input[@autocomplete='off']").send_keys('Hello world')
        self.a.find_element_by_xpath("//input[@id='su']")
if __name__ == '__main__':
    sulte=unittest.TestSuite()
    sulte.addTest(WebTest('test'))
    #testrunner=unittest.TextTestRunner()
    #runner.run(sulte)
    #按照一定的格式获取当前的时间
    now = time.strftime("%Y-%m-%d %H_%M_%S")

    #定义报告存放路径
    filename = './' + now + 'test_result.html'
    fp = open(filename,"wb")

    #定义测试报告
    runner = HTMLTestRunner(stream = fp,
                           title = "xxx接口测试报告",
                           description = "测试用例执行情况：")

    #运行测试
    runner.run(sulte)
    fp.close()              #关闭文件对象把数据写进磁盘

