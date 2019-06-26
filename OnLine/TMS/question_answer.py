from selenium import webdriver
import unittest
class Qa(unittest.TestCase):
    def setUp(self):
        self.driver.implicitly_wait(30)
        self.driver = webdriver.Chrome()
        self.driver.get('http://tms.beiwaiguoji.com/login/login')
        self.driver.maximize_window()
        self.driver.find_element_by_xpath("//input[@name='loginname']").send_keys('admin')
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys('bwgj')
        self.driver.find_element_by_name('validNumber').send_keys(6666)
        self.driver.find_element_by_xpath("//a[@class='landbtn']").click()
    def tearDown(self):
        self.driver.quit()
    def test(self):
        js = "var q=document.body.scrollTop=500"
        self.driver.execute_script(js)
        self.driver.find_element_by_xpath('//*[@id="sub_0"]/li[22]/a/span').click()
        js = "var q=document.body.scrollTop=0"
        self.driver.execute_script(js)
        self.driver.find_element_by_xpath('//*[@id="queryForm"]/div[2]/div/div[2]/button').click()
        self.driver.find_element_by_xpath('//*[@id="queryForm"]/div[2]/div/div[2]/ul/li[3]/a/label').click()
        self.driver.find_element_by_xpath('//*[@id="queryForm"]/button').click()
        Page_text=self.driver.find_element_by_xpath('//*[@id="bslist"]').text
        Page_data='没有数据！'
        file_path = r'C:\Users\Administrator\Desktop\Tms.txt'
        if Page_data in Page_text:
            print('没有待处理的问题')
        else:
            with open(file_path,'w')as fp:
                fp.write(Page_text)









        if __name__ == '__main__':
            unittest.main()