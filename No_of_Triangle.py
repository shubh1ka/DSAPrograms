def no_of_tri(arr,n):
    count=0
    for i in range(0,n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if(arr[i]+arr[j]>arr[k] and arr[j]+arr[k]>arr[i] and arr[i]+arr[k]>arr[j]):
                    count=count+1
    return count




if __name__ == '__main__':
    n=int(input())
    arr=list(map(int,input().split()))
    print(no_of_tri(arr,n))