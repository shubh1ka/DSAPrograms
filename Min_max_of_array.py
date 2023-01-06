def getMinMax(a, n):
    min = a[1]
    max = a[1]
    for i in range(0, n):
        if a[i] < min:
            min = a[i]
            i=i+1
    print(min)

    for j in range(0,n):
        if a[j]>max:
            max=a[j]
    print(max)
if __name__ == '__main__':
    n=int(input())
    a=list(map(int, input().split()))
    print(getMinMax(a , n))
