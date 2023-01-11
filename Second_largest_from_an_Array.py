def loop_for_max(a, n):
    max=a[1]
    for i in range(0,n):
        if a[i]>max:
            max=a[i]
    a.remove(max)
    max=a[1]
    for x in range(0,len(a)):
        if a[x]>max:
            max=a[x]
    return(max)


if __name__ == '__main__':
    n=int(input())
    a=list(map(int, input().split()))
    print(loop_for_max(a , n))