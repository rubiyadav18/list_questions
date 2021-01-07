x=int(input("enter a number"))
j=0
a=[]
while j<x:
    p=int(input("enter a number"))
    a.append(p)
    j=j+1
i=0
c=0
e=[ ]
e.append(a[0])
while i<len(a)-1:
    b=e[i]+1
    e.append(b)
    i=i+1
if a==e:
    print("true")
else:
    print("false")