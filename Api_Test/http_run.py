import requests
class http_run():
    def http_run(self,method,url,data=None,headers=None):
        if method=='GET':
            res=requests.get(url,data=data,headers=headers)
        else:
            res=requests.post(url,data=data,headers=headers)
        return res
