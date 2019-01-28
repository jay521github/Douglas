a=[1,2,3,4,5,11,22,333,21,45,546,76767343]
for i in range(len(a)-1,-1,-1):
    for j in range(i):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
            print(a)