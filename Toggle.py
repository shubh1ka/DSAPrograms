def sub_lists(l):
    cnt0=0
    temp0 = []
    for i in range(len(l)):
        for j in range(i+1 , len(l)+1):
            temp0 =l[i:j]
            t
        print(temp0)




# driver code
l = list(map(int, input().split()))
print(sub_lists(l))
