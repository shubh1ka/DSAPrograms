def min_dist(a, n):
    temp=[]
    dist=0
    for i in range(0,n):
        for j in range(i+1,n):
            if (a[i]==x and a[j]==y) or (a[j]==x and a[i]==y):
                dist=abs(j-i)
                temp.append(dist)
    print(min(temp))



if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().strip().split()))
    x=int(input())
    y=int(input())
    min_dist(a, n)





