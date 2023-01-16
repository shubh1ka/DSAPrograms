#enter a binart string
s=input()
res=0
for i in range(0,len(S)):
            for j in range(i+1,len(S)+1):
                a=S[i:j]
                if a.count('1')>a.count('0'):
                    res=res+1
print(res)

