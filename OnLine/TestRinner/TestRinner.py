import HTMLTestRunner
class CreatReport(object):
    def TestCaseReport(self,FailName,rect,recd,recT):
        with open('../TestReport/'+FailName+'.html','wb') as html:
            HTMLTestRunner.HTMLTestRunner(
                #文本流向
                stream=html,
                #级别
                verbosity=3,
                #标题
                title=rect,
                #描述信息
                description=recd
            ).run(recT)
