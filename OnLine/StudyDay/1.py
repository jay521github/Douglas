# for x in range(1,5):
#     for y in range(1,5):
#         for z in range(1,5):
#             if (x!=y) and (y!=z) and (z!=x):
#                 print("%d %d %d" % (x, y, z))
if __name__=="__main__":
    count=0
    for i in range(1,5):
        for j in range (1,5):
            for k in range(1,5):
                if i!=j and i!=k and j!=k:
                    print(i,j,k)
                    count+=1
    print("能组成{}个互不重复的三位数".format(count))

