import unittest
from TestRinner.TestRinner import CreatReport
from Test.TestCaseQS import TestCaseQS
def duleisi():
    a = unittest.TestSuite()
    l = ['test01']
    for j in l:
        a.addTest(TestCaseQS(j))
        FailName='自动化测试报告'
        rect='青少学习'
        recd='查看是否可以正常运行'

        CreatReport().TestCaseReport(FailName,rect,recd,a)
if __name__ == '__main__':
    duleisi()