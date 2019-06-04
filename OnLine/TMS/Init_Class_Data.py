import unittest
import requests
class init_class_data(unittest.TestCase):
    def setUp(self):
        print('Api Test Start !!!')
    def test(self):
        url='http://tms.beiwaiguoji.com/instrument/initClassData'
        params={'serialNum':'B64CZWW734','teachId':'500011'}
        res=requests.get(url=url,params=params)
        result=res.json()
        print(result)
        self.assertEqual(result["schoolTitle"],'重庆爱琴海校区',msg='error')
    def tearDown(self):
        print('Api Test end!!!')
if __name__ == '__main__':
    suite=unittest.TestSuite
    suite.addTest(init_class_data('test'))
    runner=unittest.TextTestRunner
    runner.run()


