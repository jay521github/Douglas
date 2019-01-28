import unittest
from Tools.Initialize import initialize
from Page.JwLogin import Longin
from time import sleep
from Tools.ExcelDate import Excel
from selenium.webdriver.common.action_chains import ActionChains
from Page.ClassManage import ClassManage
class JwTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver=initialize().driver
    @classmethod
    def tearDown(self):
        self.driver=initialize().driver
        #self.driver.quit()
    def test001(self):
        '''登陆'''
        self.driver.implicitly_wait(15)
        Longin().LonginName().send_keys(Excel().Ex(0,1,1))
        Longin().PassWord().send_keys(Excel().Ex(0,1,2))
        Longin().SureLongin().click()
        sleep(5)
        '''班级创建'''
        ClassManage().TeachManage().click()
        sleep(1)
        ClassManage().Classmanage().click()
        sleep(1)
        self.driver.switch_to.frame('inner-frame')
        sleep(2)
        '''班级添加'''
        ClassManage().ClassAdd().click()
        sleep(2)
        '''选择课程'''
        ClassManage().Course().click()
        sleep(3)
        ClassManage().SelectCourse().click()
        '''选择班型'''
        ClassManage().Class().click()
        sleep(3)
        SelectClass = self.driver.find_element_by_xpath("//div[@title='英标二级']")
        ActionChains(self.driver).double_click(SelectClass).perform()
        sleep(2)
        '''班级名称'''
        ClassManage().ClassName().send_keys(Excel().Ex(1,1,1))
        sleep(2)
        '''选择班主任'''
        ClassManage().ClassTeacher().click()
        sleep(3)
        SelectClassTeacher = self.driver.find_element_by_xpath('.//*[@id="listTableId_2_4786"]/tbody/tr[2]/td[2]/div/span')
        ActionChains(self.driver).double_click(SelectClassTeacher).perform()
        ClassManage().ClassRoom().click()
        sleep(2)
        '''选择教室'''
        SelectClassRoom=self.driver.find_element_by_xpath("//span[contains(.,'久凌11教')]")
        ActionChains(self.driver).double_click(SelectClassRoom).perform()
        sleep(2)
        ClassManage().Teacher().click()
        sleep(2)
        '''主讲老师'''
        SelectTeacher = self.driver.find_element_by_xpath('.//*[@id="listTableId_2_4448"]/tbody/tr[2]/td[2]/div/span')
        ActionChains(self.driver).double_click(SelectTeacher).perform()
        sleep(2)
        '''上课星期'''
        ClassManage().CourseArranging().click()
        sleep(2)
        ClassManage().SelectWeekDate().click()
        sleep(1)
        #ClassManage().ClassDate().click()
        '''设置上课时间'''
        js = "$('input[id=au_197_5027_5430]').attr('readonly',false)"
        self.driver.execute_script(js)
        self.driver.find_element_by_id('au_197_5027_5430').clear()
        self.driver.find_element_by_id('au_197_5027_5430').send_keys('08:00:00')
        # sleep(2)
        # ClassManage().SelectDate().click()
        sleep(2)
        '''保存信息'''
        ClassManage().Save().click()
        sleep(2)
        ClassManage().CourseLesson().click()
        sleep(2)
        js = "$('input[id=au_197_5117_5429]').attr('readonly',false)"
        self.driver.execute_script(js)
        self.driver.find_element_by_id('au_197_5117_5429').clear()
        self.driver.find_element_by_id('au_197_5117_5429').send_keys('2018-12-06')
        ClassManage().Save().click()



    if __name__ == '__main__':
        unittest.main()

