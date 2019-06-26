from selenium import webdriver
from OnLine.Tools.singleton import singleton
@singleton
class Login(object):
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.get('http://tms.beiwaiguoji.com/login/login')
        self.driver.maximize_window()
        self.driver.find_element_by_xpath("//input[@name='loginname']").send_keys('admin')
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys('bwgj')
        self.driver.find_element_by_name('validNumber').send_keys(6666)
        self.driver.find_element_by_xpath("//a[@class='landbtn']").click()