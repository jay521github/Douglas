from Tools.VerificationCode import VerificationCode
class CoursewarePreviewing(object):
    def __init__(self):
        self.driver=VerificationCode().driver
    def Previewing(self):
        Previewing=self.driver.find_element_by_xpath("//a[contains(.,'课件预览')]")
        return Previewing
    def CheckCourseware(self):
        CheckCourseware=self.driver.find_element_by_xpath('html/body/div[2]/div[2]/div/div[2]/div[2]/table/tbody/tr[2]/td[3]/button')
        return CheckCourseware
    def Addition(self):
        Addition=self.driver.find_element_by_xpath("//button[contains(.,'添加')]")
        return Addition
    def InputVersion(self):
        InputVersion=self.driver.find_element_by_xpath("//input[@check-type='required']")
        return InputVersion
    def Select(self):
        Select=self.driver.find_element_by_xpath("//button[@title='请选择']")
        return Select
    def SelectUnit(self):
        SelectUnit=self.driver.find_element_by_xpath("//label[contains(.,' Unit 12')]")
        return SelectUnit
    def InputUpdata(self):
        InputUpdata=self.driver.find_element_by_xpath("//textarea[@name='updateContent']")
        return InputUpdata
    def UploadFiles(self):
        UploadFiles=self.driver.find_element_by_xpath("//input[@name='file']")
        return UploadFiles
    def Sure(self):
        Sure=self.driver.find_element_by_xpath("//button[contains(.,'确定')]")
        return Sure
    def Ait(self):
        Ait=self.driver.find_element_by_xpath("//button[contains(.,'用户更新日志')]")
        return Ait
    def Back(self):
        Back=self.driver.find_element_by_xpath("//button[contains(.,'返回')]")
        return Back
    def ChickVersionNumber(self):
        ChickVersionNumber=self.driver.find_element_by_xpath("html/body/div[2]/div[2]/div/div[2]/div/table/tbody/tr[1]/td[4]")
        return ChickVersionNumber