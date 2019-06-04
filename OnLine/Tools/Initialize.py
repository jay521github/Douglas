from selenium import webdriver
from Tools.singleton import singleton
@singleton
class initialize (object):
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.get('http://oms.beiwaiguoji.com/eplus/login_page.do')
        self.driver.maximize_window()