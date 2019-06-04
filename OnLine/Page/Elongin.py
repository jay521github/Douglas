from Tools.Initialize import initialize
class longin(object):
    def __init__(self):
        self.a=initialize().driver
    def loginname(self):
        loginname=self.a.find_element_by_xpath('html/body/form/div/div[2]/p[1]/input')
        return loginname
    def password(self):
        password=self.a.find_element_by_xpath('html/body/form/div/div[2]/p[2]/input')
        return password
    def VerificationCode(self):
        VerificationCode=self.a.find_element_by_xpath('html/body/form/div/div[2]/p[3]/input')
        return VerificationCode
    def login(self):
        longin=self.a.find_element_by_xpath('html/body/form/div/div[2]/p[4]/input')
        return longin