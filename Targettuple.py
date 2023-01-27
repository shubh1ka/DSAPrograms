def res(l1,n1):
    for i in range(0,len(l1)):
        for j in range(1,len(l1)):
            if l1[i]+l1[j]==n1:
                return(l1[i],l1[j])


if __name__ == "__main__":
    l1=list(map(int,input().split()))
    n1=int(input())
    print(res(l1,n1))

