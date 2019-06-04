from OnLine.Tools.Excel import Excel
class Data(object):
    def url(self):
        url=Excel().excel(0,1)
        return url
    def loginname(self):
        loginname=Excel().excel(1,1)
        return loginname
    def Hash(self):
        Hash=Excel().excel(2,1)
        return Hash
