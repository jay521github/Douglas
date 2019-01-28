import re
s = 'daddaxxIxxdsdsdsxxLovexx5effdxxyouxxwer34'
# e = re.findall('xx.*xx',s)
# print(e)
# b = re.findall('xx.*?xx',s)
# # b = re.findall('xx(.*?)xx',s)
# print(b)
# for g in b:
#     print(g)
# a = re.search('xx(.*?)xxdsdsdsxx(.*?)xx5effdxx(.*?)xxwer34',s).group(1,2,3)
# print(a)
# for q in a:
#     print(q)
e = re.findall('(\d+)',s)
print(e)
