num=int(input("enter a numbers"))
a=1
i=0
b=0
while i<num:
    c=a+b
    a=b
    b=c
    i=i+1
print(a)