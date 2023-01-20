s=input()
tl=0
dd={"I":1,"V":5,"X":10,"C":100,"D":500,"M":1000}
for i in s:
    tl = tl+dd[i]
if "IV" in s:
    tl=tl-2
if "IX" in s:
    tl=tl-2
if "XL" in s:
    tl=tl-20
if "XC" in s:
    tl=tl-20
if "CD" in s:
    tl=tl-200
if "CM" in s:
    tl=tl-200

print(tl)

