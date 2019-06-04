from Tools.Initialize import initialize
class ClassManage(object):
    def __init__(self):
        self.driver=initialize().driver
    def TeachManage(self):
        TeachManage=self.driver.find_element_by_xpath("html/body/div[2]/div/div[1]/div[2]/div/ul/li[5]/span")
        return TeachManage
    def Classmanage(self):
        Classmanage=self.driver.find_element_by_xpath("//span[contains(.,'班级管理')]")
        return Classmanage
    def ClassAdd(self):
        ClassAdd=self.driver.find_element_by_xpath("html/body/div[1]/div[1]/div[1]/form/div[2]/span[3]/span[2]/button")
        return ClassAdd
    def Course(self):
        Course=self.driver.find_element_by_xpath('html/body/div[12]/div[2]/div[1]/form/div[1]/table/tbody/tr[2]/td[1]/div/span/input[2]')
        return Course
    def SelectCourse(self):
        SelectCourse=self.driver.find_element_by_xpath("html/body/div[16]/div/div[2]")
        return SelectCourse
    def Class(self):
        Class=self.driver.find_element_by_xpath("//input[@id='au_70_2042_1039']")
        return Class
    def ClassName(self):
        ClassName=self.driver.find_element_by_xpath("//input[@id='au_87_2034_5315']")
        return ClassName
    def ClassTeacher(self):
        ClassTeacher=self.driver.find_element_by_xpath("//input[@id='au_2_4787_5390']")
        return ClassTeacher
    def Save(self):
        Save=self.driver.find_element_by_xpath("//button[contains(.,'保存')]")
        return Save
    def ClassRoom(self):
        ClassRoom=self.driver.find_element_by_xpath("//input[@id='au_105_5025_3888']")
        return ClassRoom
    def Teacher(self):
        Teacher=self.driver.find_element_by_xpath("//input[@name='au_2_5026_3342']")
        return Teacher
    def CourseArranging(self):
        CourseArranging=self.driver.find_element_by_xpath('html/body/div[12]/div[2]/div[1]/form/div[1]/table/tbody/tr[9]/td/table/tbody/tr/td[4]/div/span[2]/input[2]')
        return CourseArranging
    def SelectWeekDate(self):
        SelectWeekDate=self.driver.find_element_by_xpath("//div[contains(.,'星期三')]")
        return SelectWeekDate
    def ClassDate(self):
        ClassDate=self.driver.find_element_by_xpath("//input[@id='au_197_5027_5430']")
        return ClassDate
    def SelectDate(self):
        SelectDate=self.driver.find_element_by_xpath("html/body/div[1]/div[2]/table/tbody/tr[2]/td")
        return SelectDate
    def CourseLesson(self):
        CourseLesson=self.driver.find_element_by_xpath('.//*[@id="listTableId_87_326"]/tbody/tr[1]/td[4]/div/a[2]')
        return CourseLesson



