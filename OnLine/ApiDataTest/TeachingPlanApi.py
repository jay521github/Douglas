import requests
import unittest
import time
from HTMLTestRunner import HTMLTestRunner
class WebRequest(unittest.TestCase):
    def setUp(self):
        self.url ='http://dev.beiwaiguoji.com/app/examinationScore/getExamScoreCount'
    def testClassTeachPlan(self):
        '''获取班级的教案列表'''
        self.r = requests.get(self.url,params={'cid':'14843','uid':'26434'})
        result = self.r.json()
        print(result)
        '''判断返回值是否成功'''
        self.assertEqual(result['result_code'],'1',msg='Error')
    def test01ResultF(self):
        self.r=requests.get(self.url,params={'cid':'0000'})
        result=self.r.text
        print(result)
        '''判断返回值为失败'''
        i=result[0]
        j='0'
        try:
            if i==j:
                print('ok')
        except:
            print('no')

    def tearDown(self):
        pass
if __name__ == '__main__':
    report = unittest.TestSuite()
    tests=[WebRequest('testClassTeachPlan'),WebRequest('test01ResultF')]
    report.addTests(tests)
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = 'D:\Html'+'now'+'ClassTeachPlan.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,title='测试报告',description='用例执行情况' )
    runner.run(report)
    fp.close()