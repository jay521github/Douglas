# -*-coding：UTF:8-*-

import unittest
#from interface.demo import RunMain   # 从之前封装的文件中，引入RunMain类
import HTMLTestRunner     # 导入HTMLTestRunner模块
import json


class TestMethod(unittest.TestCase):    # 定义一个类，继承自unittest.TestCase

    def setUp(self):
        self.run = RunMain()   # 在初始化方法中实例化一个对象，这样就不需要在每个用例中再进行实例化了

    def test01(self):
        """获取办件申请人信息"""   #在用例名下添加接口描述，可以增加测试报告可读性
        url = 'http://localhost:7001/XXX'
        data = {
            'controlSeq': '2018118325'
        }
        r = self.run.run_main(url, 'POST', data)   # 调用RunMain类中run_main方法
        print(r)
        re = json.loads(r)
        self.assertEqual(re['status'], '200', '测试失败')
        # globals()['userid'] = 22   #定义全局变量

    def test02(self):
        """查询办件进度结果信息接口"""
        # print(userid)   #使用case1中的全局变量，执行时需要全部执行，不能只执行后面的，不然会报错
        url = 'http://localhost:7001/XXX'
        data = {
            "controlSeq": "2018118325"
        }
        r = self.run.run_main(url, 'GET', data)
        print(r)
        re = json.loads(r)
        self.assertEqual(re["status"], '200', '测试失败')

    # @unittest.skip('test03')  # 跳过用例test03
    def test03(self):
        """保存办件快递信息接口(审批3.0)"""
        url = 'http://localhost:7001/XXX'
        data = {
            'controlSeq': '2018118361',
            'seq': '2939',
            'type': '1'
        }
        r = self.run.run_main(url, 'POST', data)
        print(r)
        # print(type(r)) # 查看返回对象r的类型
        re = json.loads(r)
        # print(type(re))
        self.assertEqual(re['status'], '200', '测试失败')


if __name__ == "__main__":
    # unittest.main()
    # print('__name__==__main__')
    filename = 'E:/CommonService/interface/report/testresult.html'    #测试报告的存放路径及文件名
    fp = open(filename, 'wb')    # 创测试报告html文件，此时还是个空文件

    suite = unittest.TestSuite()   # 调用unittest的TestSuite(),理解为管理case的一个容器（测试套件）
    suite.addTest(TestMethod('test01'))  # 向测试套件中添加用例，"TestMethod"是上面定义的类名，"test01"是用例名
    suite.addTest(TestMethod('test02'))
    suite.addTest(TestMethod('test03'))
    # runner = unittest.TextTestRunner()   # 执行套件中的用例
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='接口测试报告', description='测试结果如下: ')
    #  stream = fp  引用文件流
    #  title  测试报告标题
    #  description  报告说明与描述
    runner.run(suite)   # 执行测试
    fp.close()   # 关闭文件流，将HTML内容写进测试报告文件