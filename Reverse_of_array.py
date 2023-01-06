def reverse(a, n):
   a=a[::-1]
   return(a)


if __name__ == '__main__':
    n=int(input())
    a=list(map(int, input().split()))
    print(reverse(a , n))