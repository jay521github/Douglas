import unittest
import requests
'''
尝试下接口自动化  写一个小脚本

'''
class TMS(unittest.TestCase):
    def setUp(self):
        _url="http://192.168.54.212:58088/"
        parms = {"loginname" : "admin",
                 "password" :123456,
                 "JSESSIONID" :"2EC8B613C1708F3792C622F01A867A25"}
        self.requesen=requests.post(_url,data=parms,)
        self.requesen.json()
    def tearDown(self):
        pass
    def test01(self):
        pass
if __name__ == '__main__':
    unittest.main()