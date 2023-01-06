def alternateprint(arr,n):
    for i in range(0,n):
        if i%2==0:
            print(arr[i], end=" ")
if __name__ == '__main__':
    n=int(input())
    arr=list(map(int,input().split()))
    print(alternateprint(arr,n))
