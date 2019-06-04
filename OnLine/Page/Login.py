from Tools.ComfortableChange import initialize
from Tools.ExcelDate import Excel
class Login(object):
    def __init__(self):
        self.a=initialize().driver
    def LoginStart(self):
        LoginStart=self.a.find_element_by_id(Excel().Ex('LoginD',1,2))
        return LoginStart
    def LoginPasswd(self):
        LoginPasswd=self.a.find_element_by_id(Excel().Ex('LoginD',2,2))
        return LoginPasswd
    def LoginOver(self):
        LoginOver=self.a.find_element_by_id(Excel().Ex('LoginD',3,2))
        return LoginOver
