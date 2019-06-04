import unittest,requests
class Api(unittest.TestCase):
    def login(self,username,password):
        url=''
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"
        }
        params={
            'username':'username',
            'password':'password'
        }
        res=requests.get(url,params=params,headers=headers)
        result=res.text
        print(result)
        result1=res.status_code
        print(result1)
        return res.status_code
    def test1(self):
        username=''
        password=''
        result=self.login(username,password)
        self.assertEqual(200,result)
if __name__ == '__main__':
    unittest.main()
