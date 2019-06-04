import re
s = 'daddaxxIxxdsdsdsxxLovexx5effdxxyouxxwer34'
a = re.search('xx(.*?)xxdsdsdsxx(.*?)xx5effdxx(.*?)xxwer34',s).group(1,2,3)
print(a)
for q in a:
    print(q)
# e = re.findall('(\d+)',s)
#print(e)
