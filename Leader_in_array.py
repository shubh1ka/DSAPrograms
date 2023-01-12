def LeadArr(a, n):
    for i in range(0,n):
        for j in range(i+1,n):
            if a[i]<=a[j]:
                break
        if j==(n-1):
            print(a[i],end=' ')



if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().strip().split()))
    (LeadArr(a, n))

