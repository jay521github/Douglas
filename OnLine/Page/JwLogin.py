from Tools.Initialize import initialize
class Longin(object):
    def __init__(self):
        self.driver=initialize().driver
    def LonginName(self):
        LonginName=self.driver.find_element_by_xpath("//input[@id='loginName']")
        return LonginName
    def PassWord(self):
        PassWord=self.driver.find_element_by_xpath("//input[@id='password']")
        return PassWord
    def SureLongin(self):
        SureLogin=self.driver.find_element_by_xpath("//input[@onclick='loginWeb();']")
        return SureLogin