import unittest
import requests
from HTMLTestRunner import HTMLTestRunner
class TryApi(unittest.TestCase):
    def setUp(self):
        self.url='http://dev.beiwaiguoji.com/instrument/initClassData'
    def tearDown(self):
        pass
    def testClassData(self):
        '''班级学员接口测试'''
        self.r = requests.post(self.url, data={'serialNum': 'H959F6K24J', 'teachId': '39190'})
        result=self.r.json()
        print(result)
        self.assertEqual(result['classStatus'],2,msg='classStatus is  Error')
if __name__ == '__main__':
    TestReport=unittest.TestSuite()
    TestReport.addTest(TryApi('testClassData'))
    filepath='D:\Html\\TestReport.html'
    fp=open(filepath,'wd')
    runner=HTMLTestRunner(stream=fp,verbosity=3,title='班级信息接口测试报告',description='接口测试')
    runner.run(TestReport)
    fp.close()
