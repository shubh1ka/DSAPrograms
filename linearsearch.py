if __name__ == '__main__':
    arr=list(map(int,input().split()))
    x=int(input())
    index=0
    for i in range(0,len(arr)):
        if arr[i]==x:
            index=1
            print(i)
    if index==0:
        print(-1)
