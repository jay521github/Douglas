import unittest
from Api_Test.http_run import http_run
class Api_Test_Case(unittest.TestCase):
    def setUp(self):
        print('测试开始')
        self.run=http_run()
    def test_get(self):
        url1='http://tms.beiwaiguoji.com/instrument/initClassData?serialNum=B64CZWW734&teachId=63167'
        res=self.run.http_run('GET',url1)
        print(res.json())
    def test_post(self):
        url2='http://tms.beiwaiguoji.com/app/teachingPlan/getTpOfWeekJSON'
        data = {'id': '1054958'}
        res=self.run.http_run('POST',url2,data)
        print(res.json())
    def tearDown(self):
        print('测试结束')
if __name__ == '__main__':
    suit=unittest.TestSuite()
    suit.addTest(Api_Test_Case('test_get'))
    # suit.addTest(Api_Test_Case('test_post'))
    runner=unittest.TextTestRunner()
    runner.run(suit)
