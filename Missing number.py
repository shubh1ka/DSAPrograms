def Missingnumber(n, arr):

    s=(n*(n+1))//2
    sm=sum(arr)
    if (s-sm)!=0:
        return (s-sm)
    else:
        return("No Number Missing")
if __name__ == '__main__':
    n = int(input())
    arr=list(map(int , input().split()))

    print(Missingnumber(n,arr))
