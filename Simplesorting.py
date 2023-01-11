a=[22,3,31,5,7,11,1]
i=0
for j in range(1,len(a)):
    for i in range(0,j):
        if a[j]<a[i]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print(a)
