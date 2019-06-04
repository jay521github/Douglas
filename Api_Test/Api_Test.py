import requests
import unittest
import HTMLTestRunner
from Api_Test.Data import Data
import os
import time
class Api_Test(unittest.TestCase):
    def setUp(self):
        pass
    def test(self):
        res=requests.get(url=Data().url(),params={'loginname':Data().loginname(),'Hash':Data().Hash()})
        result=res.text
        print(result)
        try:
            assert '59136' in result
            print('ok')
        except Exception as e:
            print(e)
            print('No')
    def tearDown(self):
        pass
if __name__ == '__main__':
    suite=unittest.TestSuite()
    suite.addTest(Api_Test('test'))
    now=time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    path=r'C:\Users\Administrator\Desktop\Data'
    filepath=os.path.join(path,'resule_'+now+'.html')
    fp=open(filepath,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=5,title='Test',description='Test')
    runner.run(suite)
    fp.close()