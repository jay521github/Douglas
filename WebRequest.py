import requests
url="http://192.168.54.212:58088/"
r=requests.get(url,params={"admin":'123456'})
result=r.json()
assert result['status']==200