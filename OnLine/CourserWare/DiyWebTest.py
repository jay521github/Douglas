from Tools.VerificationCode import VerificationCode
import unittest
from time import sleep
from Page.CoursewarePreviewing import CoursewarePreviewing
class DiyWebTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver=VerificationCode().driver
    @classmethod
    def tearDown(self):
        self.driver=VerificationCode().driver
        self.driver.quit()
    def test01(self):
        self.driver.implicitly_wait(10)
        sleep(2)
        CoursewarePreviewing().Previewing().click()#点击课件预览
        sleep(2)
        CoursewarePreviewing().CheckCourseware().click()#点击课件
        sleep(2)
        CoursewarePreviewing().Ait().click()  # 查看用户更新日志
        sleep(2)
        VersionNumber=CoursewarePreviewing().ChickVersionNumber().text
        print(VersionNumber)
        sleep(2)
        CoursewarePreviewing().Back().click()
        sleep(1)
        CoursewarePreviewing().Addition().click()#添加
        sleep(2)
        CoursewarePreviewing().InputVersion().send_keys(VersionNumber+'.1')
        # try:
        #     if VersionNumber==VN:
        #         CoursewarePreviewing().InputVersion().send_keys(VN+'.1')
        # except:
        #     CoursewarePreviewing().InputVersion().send_keys(VN)#填写版本号
        sleep(1)
        CoursewarePreviewing().Select().click()#选择
        sleep(1)
        CoursewarePreviewing().SelectUnit().click()#选择单元
        sleep(1)
        CoursewarePreviewing().InputUpdata().send_keys('Test')#输入更新内容
        CoursewarePreviewing().UploadFiles().send_keys('D:\\Unit 12.txt')#上传课件
        sleep(1)
        CoursewarePreviewing().Sure().click()#点击确认

if __name__ == '__main__':
    unittest.main()