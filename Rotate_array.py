def rotate(a, n,d):
    l=[]
    l=a[d::]+a[:d:]
    #print(a[0:3])


    print(l)



if __name__ == '__main__':
    n=int(input())
    d=int(input())
    a=list(map(int, input().split()))
    print(rotate(a , n,d))