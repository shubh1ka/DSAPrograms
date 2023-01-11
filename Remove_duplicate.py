def remove_dup(a,n):
        i=0
        for j in range(1,n):
            if a[i]!=a[j]:
                i=i+1
                a[i]=a[j]

        return(i+1)


if __name__ == '__main__':
    n=int(input())
    a=list(map(int, input().strip().split()))
    N= remove_dup(a,n)
    for x in range(N):
        print(a[x],end= " ")



