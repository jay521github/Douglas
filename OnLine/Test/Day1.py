import requests
url='http://dev.beiwaiguoji.com/index/managerIndex'
r=requests.get(url,params={'loginname':'admin','password':'123456'})
data=r.text
print(data)