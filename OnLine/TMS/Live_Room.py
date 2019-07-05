from selenium import webdriver
import unittest
from time import sleep
class live_room(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get('http://172.17.15.172:8082/login/login')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/ul/li[1]/input').send_keys('admin')
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/ul/li[2]/input').send_keys('bwgj')
        self.driver.find_element_by_xpath('//*[@id="validNumber"]').send_keys('6666')
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/a').click()
    def tearDown(self):
        self.driver.quit()
    def test(self):
        self.driver.find_element_by_xpath('//*[@id="sidebar"]/ul/li[5]/a').click()
        self.driver.find_element_by_xpath('//*[@id="sub_4"]/li[1]/a').click()
        text_list=self.driver.find_element_by_xpath('//*[@id="broadcastClassbslist"]/table/tbody').text
        text='尹志平君子之道'
        if text in text_list:
            self.driver.find_element_by_xpath('//*[@id="broadcastClassbslist"]/table/tbody/tr[7]/td[15]/button[3]').click()
            self.driver.switch_to.window('http://beiwaiguoji.at.baijiayun.com/web/room/prepare?room_id=19070454001070&code=m965pa&urlType=3580kcehju')
            sleep(5)
            self.driver.find_element_by_xpath('//*[@id="inputForm"]/div[1]/div/div/button').click()
            self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div[3]/img').click()
            self.driver.find_element_by_xpath('//*[@id="bjy-join-class-dialog"]/div/div[3]').click()
            print('打开直播间')
        else:
            print('没有找到直播间')

if __name__ == '__main__':
    unittest.main()