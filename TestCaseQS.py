import unittest
from Tools.ComfortableChange import initialize
from Page.Login import Login
from Page.HomePage import HomePage
from Page.StudyPage import StudyPage
from Page.Bake import Bake
from time import sleep
class TestCaseQS(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.a=initialize().driver
    @classmethod
    def tearDown(cls):
        cls.a=initialize().driver
        cls.a.quit()
    def test01(self):
        #滑屏
        sleep(5)
        self.a.swipe(700, 500, 100, 500, 1000)
        self.a.swipe(700, 500, 100, 500, 1000)
        self.a.swipe(700, 500, 100, 500, 1000)
        self.a.swipe(700, 500, 100, 500, 1000)
        self.a.swipe(800, 500, 100, 500, 1000)
        sleep(3)
        self.a.swipe(800, 500, 100, 500, 1000)
        sleep(3)
        self.a.find_element_by_class_name('android.widget.Button').click()
        sleep(5)
       #登陆用户名
        Login().LoginStart().send_keys('zhangkairui1')
        #登陆密码
        sleep(2)
        Login().LoginPasswd().send_keys('123456')
        #点击登陆
        sleep(2)
        Login().LoginOver().click()
        # 首页
        sleep(2)
        #点击学习
        HomePage().Study().click()
        sleep(2)
        #确认按钮
        HomePage().Sure().click()
        #学习页面
        sleep(5)
        StudyPage().SelectClass().click()
        sleep(6)
        StudyPage().SelectClassHour().click()
        sleep(5)
        self.a.swipe(500, 1000, 500, 100, 1000)
        # self.a.swipe(500, 1000, 500, 100, 1000)
        sleep(2)
        self.a.tap([(114,1633)])
        sleep(10)
        self.a.tap([(114,1633)])
        sleep(2)
        #返回首页
        Bake().Bake().click()
        sleep(2)
        Bake().Bake().click()
        sleep(3)
        self.a.find_element_by_id('com.ihimee.bwqs:id/main_tab_settings').click()
        a=self.a.find_element_by_id('com.ihimee.bwqs:id/user_name').text
        b='张凯瑞zhangkairui'
        self.assertEqual(b,a,msg='登陆成功')
# if __name__ == '__main__':
#     unittest.main()
