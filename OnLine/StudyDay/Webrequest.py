import requests
import unittest
from HTMLTestRunner import HTMLTestRunner
class WebRequest(unittest.TestCase):
    def setUp(self):
        self.url ='http://dev.beiwaiguoji.com/instrument/downloadGame/'
    def tearDown(self):
        pass
    def testDownGame(self):
        '''测试游戏下载接口'''
        self.r = requests.get(self.url,params={'dateTime':'1539412530','serialNumber':'B64CZWW734','uploadName':'shangchao'})
        result = self.r.json()
        print(result)
        self.assertEqual(result['title'], '游戏更新No1',msg='fail')
        self.assertEqual(result['uploadText'],'测试')
if __name__ == '__main__':
    report = unittest.TestSuite()
    report.addTest(WebRequest('testDownGame'))
    filename = 'D:\Html\\result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,title='测试报告',description='用例执行情况' )
    runner.run(report)
    fp.close()
